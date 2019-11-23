import requests
import os
import threading
import sys

node_name = sys.argv[1]
n_threads = 2 * int(sys.argv[2])

volatile_dir = '/volatile/m139t745/npm-packages'

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def thread_start(packages):
    for package in packages:
        try:
            package_name = package[:-1]

            if '*' in package_name:
                continue

            dir_name = package_name.replace('/', '~')
            metadata_request = requests.get('https://registry.npmjs.org/{}'.format(package_name))

            if metadata_request.status_code != 200:
                print('Error: metadata request for {} returned {}'.format(package_name, metadata_request.status_code))
                continue

            metadata = metadata_request.json()

            latest_version = ''
            latest_time = ''
            all_times = metadata['time']

            for time in all_times:
                if time == 'modified' or time == 'created' or time == '0.0.1-security' or time == '0.0.2-security':
                    continue

                if (latest_version == '' and latest_time == '') or (all_times[time] > latest_time):
                    latest_version = time
                    latest_time = all_times[time]

            if latest_version == '':
                continue

            latest_url = metadata['versions'][latest_version]['dist']['tarball']

            source_code_request = requests.get(latest_url)

            if source_code_request.status_code != 200:
                print('Error: source code status request for {} returned {}'.format(package_name, source_code_request.status_code))
                continue

            # if this is a new package, make a new directory
            if not os.path.isdir('{}/{}'.format(volatile_dir, dir_name)):
                os.mkdir('{}/{}'.format(volatile_dir, dir_name))

            # if the newest version hasn't already been downloaded
            if '{}.tgz'.format(latest_version) not in os.listdir('{}/{}'.format(volatile_dir, dir_name)):
                # remove any previous versions
                for old_version in os.listdir('{}/{}'.format(volatile_dir, dir_name)):
                    os.system('rm {}/{}/{}'.format(volatile_dir, dir_name, old_version))

                # download latest version
                with open('{}/{}/{}.tgz'.format(volatile_dir, dir_name, latest_version), 'wb') as f:
                    f.write(source_code_request.content)

        except:
            print('Error: unhandled exception when processing {}'.format(package_name))
            

all_packages = open('/users/m139t745/npm-analysis/download_all_packages/package_names/{}'.format(node_name)).readlines()
threads = []
all_chunks = chunks(all_packages, int(len(all_packages) / n_threads) + 1)

for i in range(n_threads):
    chunk = next(all_chunks)
    threads.append(threading.Thread(target=thread_start, args=(chunk,)))
    threads[i].start()

for i in range(n_threads):
    threads[i].join()
