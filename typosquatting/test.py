import pandas as pd
from typosquatting import *
from fuzzyset import FuzzySet
import json
import threading

n_threads = 20
popular_package_weekly_download_cutoff = 10000
lock = threading.Lock()

downloads_df = pd.read_csv('../data/downloads.csv', na_filter=False)
popular_packages = set(downloads_df.loc[downloads_df.weekly_downloads > popular_package_weekly_download_cutoff].package_name.values)

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

# typosquatting_df = pd.read_csv('../data/typosquatting_examples.csv')
all_package_names = list(set([x['id'] for x in json.load(open('_all_docs.json'))['rows']]) - popular_packages)
fuzzy_package_names = FuzzySet(popular_packages)

log = open('output', 'w')
log.write('package_name,repeated_characters,omitted_characters,rearranged_characters,swapped_characters,swapped_words,detect_typos,highest_ratio_package,fuzzywuzzy_ratio,fuzzyset_match,fuzzyset_ratio\n')

def run_check(malicious_package_name, f):
    result = ''
    for popular_package in popular_packages:
        if f(malicious_package_name, popular_package):
            result = popular_package
            break

    if result == '':
        return 'n/a,'
    else:
        return '{},'.format(result)

def thread_start(packages):
    for package_name in packages:
        message = '{},'.format(package_name)

        message += run_check(package_name, repeated_characters)
        message += run_check(package_name, omitted_characters)
        message += run_check(package_name, rearranged_characters)
        message += run_check(package_name, swapped_characters)
        message += run_check(package_name, swapped_words)
        message += run_check(package_name, detect_typos)

        most_similar_package_name = highest_ratio(package_name, popular_packages)
        message += '{},{},'.format(most_similar_package_name[0], most_similar_package_name[1])

        fuzzyset_result = fuzzy_package_names.get(package_name)
        
        if fuzzyset_result == None:
            message += 'n/a,n/a'
        else:
            message += '{},{}'.format(fuzzyset_result[0][1], fuzzyset_result[0][0])

        lock.acquire()
        log.write('{}\n'.format(message))
        log.flush()
        lock.release()

threads = []
all_chunks = chunks(all_package_names, int(len(all_package_names) / (n_threads + 1)))

for _ in range(n_threads):
    current_chunk = next(all_chunks)
    t = threading.Thread(target=thread_start, args=(current_chunk,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

log.close()