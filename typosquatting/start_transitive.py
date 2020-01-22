import os
import sys
import ast
import subprocess
import threading

lock = threading.Lock()

node = sys.argv[1]
n_threads = sys.argv[2]

os.system('rm -rf /dev/shm/npm')
os.system('mkdir -p /dev/shm/npm/transitive')
os.system('mkdir /dev/shm/npm/data')
os.system('cp ../data/typosquatting_candidates.txt /dev/shm/npm/data')

positive_log = open('/dev/shm/npm/transitive/positive', 'w')
negative_log = open('/dev/shm/npm/transitive/negative', 'w')

typosquatting_candidates = set(open('/dev/shm/npm/data/typosquatting_candidates.txt').read().splitlines())

machine_packages = open('/users/m139t745/npm-analysis/typosquatting/transitive_package_names/{}'.format(node)).read().splitlines()


def start_thread(packages):
    for package_name in packages:

        if package_name in typosquatting_candidates:
            lock.acquire()
            positive_log.write('{}\n'.format(package_name))
            positive_log.flush()
            lock.release()
            continue

        result = subprocess.check_output('npm-remote-ls -n {} -f -d false'.format(package_name), shell=True).decode('utf8')

        # remove any error text
        bracket_index = result.rfind('[')
        result = result[bracket_index:]

        try:
            typosquatting = False
            raw_dependencies = ast.literal_eval(result)
            for dependency in raw_dependencies:
                if dependency[0] == '@':
                    at_index = dependency.find('@', 1)
                    clean_dependency = dependency[:at_index]
                else:
                    clean_dependency = dependency.split('@')[0]

                if clean_dependency in typosquatting_candidates:
                    typosquatting = True
                    lock.acquire()
                    positive_log.write('{}\n'.format(package_name))
                    positive_log.flush()
                    lock.release()
                    break

            if not typosquatting:
                lock.acquire()
                negative_log.write('{}\n'.format(package_name))
                negative_log.flush()
                lock.release()

        except:
            lock.acquire()
            negative_log.write('{}\n'.format(package_name))
            negative_log.flush()
            lock.release()


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

all_chunks = chunks(machine_packages, int(len(machine_packages) / n_threads) + 1)
threads = []

for _ in range(n_threads):
    chunk = next(all_chunks)
    t = threading.Thread(target=start_thread, args=(chunk,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

positive_log.close()
negative_log.close()

os.system('mv /dev/shm/npm/transitive/positive /users/m139t745/npm-analysis/typosquatting/transitive_output/positive/{}'.format(node))
os.system('mv /dev/shm/npm/transitive/negative /users/m139t745/npm-analysis/typosquatting/transitive_output/negative/{}'.format(node))
os.system('rm -rf /dev/shm/npm')
