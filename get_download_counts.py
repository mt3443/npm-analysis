import requests
import json
import os
import threading
import time

n_threads = 20
lock = threading.Lock()

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

print('Reading all docs', flush=True)
all_packages = [x['id'] for x in json.load(open('_all_docs.json'))['rows']]
all_packages = set(all_packages)


print('Parsing already processed', flush=True)
processed_packages = open('downloads.csv').readlines()
processed_packages = [x.split(',')[0] for x in processed_packages]

print('Removing already processed', flush=True)
for p in processed_packages:
    all_packages.remove(p)

downloads_endpoint = 'https://api.npmjs.org/downloads/point/last-week'

results = open('package_downloads.csv', 'w')

def log(m):
    lock.acquire()
    results.write('{}\n'.format(m))
    results.flush()
    lock.release()

def start(packages):
    for package_name in packages:

        try:
            r = requests.get('{}/{}'.format(downloads_endpoint, package_name))

            if r.status_code == 429:
                while r.status_code == 429:
                    time.sleep(30)
                    r = requests.get('{}/{}'.format(downloads_endpoint, package_name))
            
            if r.status_code != 200:
                print('ERROR: status code {} returned for {}'.format(r.status_code, package_name))
                continue

            log('{},{}'.format(package_name, r.json()['downloads']))

        except Exception as e:
            print('ERROR: unhandled exception when processing {}'.format(package_name))
            print(e)

threads = []

packages_per_thread = int(len(all_packages) / (n_threads + 1))
all_chunks = chunks(list(all_packages), packages_per_thread)

print('Processing', flush=True)
for i in range(n_threads):
    chunk = next(all_chunks)
    t = threading.Thread(target=start, args=(chunk,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

results.close()