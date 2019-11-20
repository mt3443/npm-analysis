import os
import subprocess
import threading
import sys
import json
from dangerous import *
from get_called_functions import get_called_functions

# Globals
script_id = sys.argv[1]
n_threads = int(sys.argv[2])

column_headers = 'package_name,version,has_scripts,has_install_scripts,dangerous_install_scripts,n_js_files,jast_result,calls_dangerous_functions'

working_dir = '/dev/shm/npm_{}'.format(script_id)
network_dir = '/users/m139t745/npm-analysis'
volatile_dir = '/volatile/m139t745'

all_packages = open('{}/package_names/{}'.format(network_dir, script_id), 'r').readlines()
lock = threading.Lock()
log_file = open('{}/output/{}'.format(network_dir, script_id), 'w')

install_scripts = ['preinstall', 'install', 'postinstall', 'preuninstall', 'uninstall', 'postuninstall']


# Top level function, starts and joins threads
def main():
    init()
    threads = []
    all_chunks = chunks(all_packages, int(len(all_packages) / n_threads) + 1)

    for i in range(n_threads):
        chunk = next(all_chunks)
        threads.append(threading.Thread(target=thread_start, args=(chunk, i,)))
        threads[i].start()

    for i in range(n_threads):
        threads[i].join()


# General setup. Creates directories, files, etc. needed for analysis
def init():
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

    if not os.path.exists('{}/output'.format(network_dir)):
        os.mkdir('{}/output'.format(network_dir))

    if not os.path.exists('{}/malicious_packages'.format(network_dir)):
        os.mkdir('{}/malicious_packages'.format(network_dir))


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

            # remove any leftover copies of the package from the working dir
            if os.path.exists('{}/packages_temp/{}'.format(working_dir, dir_name)):
                os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))

            # copy package from volatile drive, extract contents
            os.mkdir('{}/packages_temp/{}'.format(working_dir, dir_name))
            os.system('cp {}/npm-packages/{}/*.tgz {}/packages_temp/{}'.format(volatile_dir, dir_name, working_dir, dir_name))
            os.system('tar zxf {}/packages_temp/{}/*.tgz -C {}/packages_temp/{} > /dev/null 2>&1'.format(working_dir, dir_name, working_dir, dir_name))

            # directory in tarball is not always named 'package', find whatever it's called
            package_dir_name = subprocess.check_output('ls -d {}/packages_temp/{}/*/'.format(working_dir, dir_name), shell=True).decode('utf8')[:-1]

            # get a list of all javascript files
            os.system('chmod -R 777 {}'.format(package_dir_name))
            os.system('find {} -type f -name "*.js" >> {}/packages_temp/{}/js_files'.format(package_dir_name, working_dir, dir_name))
            js_files = open('{}/packages_temp/{}/js_files'.format(working_dir, dir_name), 'r').readlines()

            # run tests, record results
            jast_output = jast(js_files, dir_name, thread_id)

            metadata = json.load(open('{}/package.json'.format(package_dir_name), 'r'))
            row = metadata['name'] + ',' + metadata['version'] + ','

            row += has_scripts(metadata) + ','
            row += has_install_scripts(metadata) + ','
            row += dangerous_install_scripts(metadata) + ','
            row += str(len(js_files)) + ','
            row += jast_output + ','
            row += calls_dangerous_functions(js_files)

            log(row)

            if jast_output == 'malicious':
                os.system('rm -rf {}'.format(package_dir_name))
                os.system('mv {}/packages_temp/{} {}/malicious_packages'.format(working_dir, dir_name, network_dir))
            else:
                os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))

        except Exception as e:
            # print('ERROR: unhandled exception when processing {}'.format(package_name))
            print(e)
            continue


def has_scripts(metadata):
    return 'yes' if 'scripts' in metadata else 'no'


def has_install_scripts(metadata):
    if 'scripts' not in metadata:
        return 'no'

    for script in install_scripts:
        if script in metadata['scripts']:
            return 'yes'

    return 'no'


def dangerous_install_scripts(metadata):
    if 'scripts' not in metadata:
        return 'no'

    for script in install_scripts:
        if script in metadata['scripts']:
            parts = metadata['scripts'][script].split()

            for part in parts:
                if part in dangerous_commands:
                    return 'yes'

    return 'no'
    

# Searches for malicious syntax using jast
# param: js_files, list of javascript files to scan
# param: dir_name, where to save jast output file
# param: thread_id, thread identifier used to indicate which jast model to use
# return: string, 'malicious' or 'benign'
def jast(js_files, dir_name, thread_id):
    if len(js_files) == 0:
        return 'benign'

    # run jast on all files in js_files list
    for js_file in js_files:
        os.system('python3 {}/jast_models/{}/clustering/classifier.py --v 5 --m {}/jast_models/{}/Classification/model --f "{}" >> {}/packages_temp/{}/jast_output'.format(working_dir, thread_id, working_dir, thread_id, js_file[:-1], working_dir, dir_name))

    # get number of files classified as malicious
    result = subprocess.check_output('grep ": malicious" {}/packages_temp/{}/jast_output | wc -l'.format(working_dir, dir_name), shell=True)
    n_malicious = int(result.decode('utf8'))

    if n_malicious == 0:
        return 'benign'
    else:
        return 'malicious'


def calls_dangerous_functions(js_files):
    called_functions = get_called_functions(js_files)

    for function in called_functions:
        if function in dangerous_functions:
            return 'yes'

    return 'no'


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    main()
