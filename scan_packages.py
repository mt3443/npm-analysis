import os
import subprocess
import threading
import sys

script_id = sys.argv[1]
n_threads = int(sys.argv[2])

working_dir = '/dev/shm/npm_{}'.format(script_id)
network_dir = '/users/m139t745/npm-analysis'
volatile_dir = '/volatile/m139t745'

if not os.path.exists(working_dir):
    os.mkdir(working_dir)

if not os.path.exists('{}/jast_models'.format(working_dir)):
    os.mkdir('{}/jast_models'.format(working_dir))

if not os.path.exists('{}/packages_temp'.format(working_dir)):
    os.mkdir('{}/packages_temp'.format(working_dir))

for i in range(n_threads):
    if not os.path.exists('{}/jast_models/{}'.format(working_dir, i)):
        os.mkdir('{}/jast_models/{}'.format(working_dir, i))
        os.system('cp -r {}/jast/* {}/jast_models/{}'.format(network_dir, working_dir, i))

all_packages = open('{}/package_names/{}'.format(network_dir, script_id), 'r').readlines()

lock = threading.Lock()

if not os.path.exists('{}/output'.format(network_dir)):
    os.mkdir('{}/output'.format(network_dir))

if not os.path.exists('{}/malicious_packages'.format(network_dir)):
    os.mkdir('{}/malicious_packages'.format(network_dir))

log_file = open('{}/output/{}'.format(network_dir, script_id), 'w')

def log(message):
    lock.acquire()
    log_file.write(message + '\n')
    log_file.flush()
    lock.release()

def thread_start(packages, thread_id):

    for package in packages:

        try:
            dir_name = package[:-1]
            package_name = dir_name.replace('~', '/')

            if os.path.exists('{}/packages_temp/{}'.format(working_dir, dir_name)):
                os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))

            os.mkdir('{}/packages_temp/{}'.format(working_dir, dir_name))
            os.system('cp {}/npm-packages/{}/*.tgz {}/packages_temp/{}'.format(volatile_dir, dir_name, working_dir, dir_name))
            os.system('tar zxf {}/packages_temp/{}/*.tgz -C {}/packages_temp/{} > /dev/null 2>&1'.format(working_dir, dir_name, working_dir, dir_name))

            package_dir_name = subprocess.check_output('ls -d {}/packages_temp/{}/*/'.format(working_dir, dir_name), shell=True).decode('utf8')[:-1]

            os.system('chmod -R 777 {}'.format(package_dir_name))
            os.system('find {} -type f -name "*.js" >> {}/packages_temp/{}/js_files'.format(package_dir_name, working_dir, dir_name))

            js_files = open('{}/packages_temp/{}/js_files'.format(working_dir, dir_name), 'r').readlines()

            if len(js_files) == 0:
                os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))
                log('BENIGN: {}, no js files'.format(package_name))
                continue

            for js_file in js_files:
                os.system('python3 {}/jast_models/{}/clustering/classifier.py --v 5 --m {}/jast_models/{}/Classification/model --f "{}" >> {}/packages_temp/{}/output'.format(working_dir, thread_id, working_dir, thread_id, js_file[:-1], working_dir, dir_name))

            if not os.path.exists('{}/packages_temp/{}/output'.format(working_dir, dir_name)):
                os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))
                log('ERROR: could not find jast output file for {}'.format(package_name))
                continue

            result = subprocess.check_output('grep ": malicious" {}/packages_temp/{}/output | wc -l'.format(working_dir, dir_name), shell=True)
            n_malicious = int(result.decode('utf8'))

            if n_malicious == 0:
                os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))
                log('BENIGN: {}, no malicious js files found'.format(package_name))
            else:
                os.system('mv {}/packages_temp/{} {}/malicious_packages'.format(working_dir, dir_name, network_dir))
                log('MALICIOUS: {}'.format(package_name))

        except:
            log('ERROR: unhandled exception when processing {}'.format(package_name))
            continue

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

threads = []

all_chunks = chunks(all_packages, int(len(all_packages) / n_threads) + 1)

for i in range(n_threads):
    chunk = next(all_chunks)
    threads.append(threading.Thread(target=thread_start, args=(chunk, i,)))
    threads[i].start()


for i in range(n_threads):
    threads[i].join()
