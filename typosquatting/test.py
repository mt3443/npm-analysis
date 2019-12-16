import pandas as pd
from typosquatting import *

popular_package_weekly_download_cutoff = 10000

downloads_df = pd.read_csv('../data/downloads.csv', na_filter=False)
popular_packages = downloads_df.loc[downloads_df.weekly_downloads > popular_package_weekly_download_cutoff].package_name.values
del downloads_df

typosquatting_df = pd.read_csv('../data/typosquatting_examples.csv')

log = open('output', 'w')
log.write('malicious_package_name,benign_package_name,repeated_characters,omitted_characters,rearranged_characters,swapped_characters,swapped_words,detect_typos,highest_ratio_package,ratio\n')

def run_check(malicious_package_name, f):
    result = ''
    for popular_package in popular_packages:
        if f(malicious_package_name, popular_package):
            result = popular_package
            break

    if result == '':
        log.write('n/a,')
    else:
        log.write('{},'.format(result))

for index, row in typosquatting_df.iterrows():
    malicious_package_name = row['malicious_package_name']
    benign_package_name = row['benign_package_name']

    log.write('{},{},'.format(malicious_package_name, benign_package_name))

    run_check(malicious_package_name, repeated_characters)
    run_check(malicious_package_name, omitted_characters)
    run_check(malicious_package_name, rearranged_characters)
    run_check(malicious_package_name, swapped_characters)
    run_check(malicious_package_name, swapped_words)
    run_check(malicious_package_name, detect_typos)

    most_similar_package_name = highest_ratio(malicious_package_name, popular_packages)

    log.write('{},{}\n'.format(most_similar_package_name[0], most_similar_package_name[1]))

    log.flush()

log.close()
    
