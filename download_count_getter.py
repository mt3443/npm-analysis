import requests
import time
import sys
import os

downloads_endpoint = 'https://api.npmjs.org/downloads/point/last-week'
all_packages = [x[:-1] for x in open('/users/m139t745/npm-analysis/download_package_names/{}'.format(sys.argv[1])).readlines()]

success = open('/dev/shm/success', 'w')
fail = open('/dev/shm/fail', 'w')

for package_name in all_packages:
    try:
        r = requests.get('{}/{}'.format(downloads_endpoint, package_name))

        if r.status_code == 429:
            while r.status_code == 429:
                time.sleep(30)
                r = requests.get('{}/{}'.format(downloads_endpoint, package_name))
        
        if r.status_code != 200:
            fail.write('{} returned {}'.format(package_name, r.status_code))
            fail.flush()
            continue

        success.write('{},{}'.format(package_name, r.json()['downloads']))
        success.flush()

    except Exception as e:
        fail.write('{} error'.format(package_name))
        fail.flush()

os.system('mv /dev/shm/success /users/m139t745/npm-analysis/data/download_counts/success/{}'.format(sys.argv[1]))
os.system('mv /dev/shm/fail /users/m139t745/npm-analysis/data/download_counts/fail/{}'.format(sys.argv[1]))
