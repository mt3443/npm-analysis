import os
import subprocess
import json
import sys
import threading
import editdistance
import datetime
import pandas as pd
from get_called_functions import get_called_functions
from socket import socket, AF_INET, SOCK_STREAM

script_id = sys.argv[1]
n_threads = 4

port = 3443
server_ip = '10.123.131.77'
buffer_size = 1024

column_headers = """package_name,
                    version,
                    has_scripts,
                    has_install_scripts,
                    curl_in_install_scripts,
                    wget_in_install_scripts,
                    rm_in_install_scripts,
                    n_js_files,
                    jast_result,
                    eval_calls,
                    networking_calls,
                    new_package_1_week,
                    possibly_typosquatting,
                    typosquatting_target"""

working_dir = '/dev/shm/npm_{}'.format(script_id)
network_dir = '/users/m139t745/npm-analysis'
volatile_dir = '/volatile/m139t745'

log_file = open('{}/output/{}'.format(network_dir, script_id), 'w')
error_file = open('{}/errors/{}'.format(network_dir, script_id), 'w')

lock = threading.Lock()

install_scripts = ['preinstall', 'install', 'postinstall', 'preuninstall', 'uninstall', 'postuninstall']
networking_functions = ['get', 'put', 'post', 'then', 'fetch', 'encodeURIComponent', 'unescape']

df = pd.read_csv('data/downloads.csv', na_filter=False)
popular_packages = set(df.loc[df['weekly_downloads'] > 10000]['package_name'].values)

today = datetime.datetime.today()


# Starts threads
def main():
    threads = []

    for i in range(n_threads):
        thread = threading.Thread(target=start_worker, args=(i,))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    os.system('rm -rf {}'.format(working_dir))


# General setup. Creates directories, files, etc. needed for analysis
def init():
    if os.path.exists(working_dir):
        os.system('chmod -R 777 {}'.format(working_dir))
        os.system('rm -rf {}'.format(working_dir))

    os.mkdir(working_dir)
    os.mkdir('{}/packages_temp'.format(working_dir))
    os.mkdir('{}/jast_models'.format(working_dir))

    for i in range(n_threads):
        os.system('cp -r {}/jast {}/jast_models/{}'.format(network_dir, working_dir, i))


def log(message):
    lock.acquire()
    log_file.write(message + '\n')
    log_file.flush()
    lock.release()


def start_worker(thread_id):

    while True:
        message = 'request'
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_ip, port))
        client_socket.send(message.encode('utf8'))
        response = client_socket.recv(buffer_size).decode('utf8')
        client_socket.close()

        if response == 'no packages remaining':
            return

        try:
            dir_name = response
            package_name = dir_name.replace('~', '/')

            # remove any leftover copies of the package from the working dir
            if os.path.exists('{}/packages_temp/{}'.format(working_dir, dir_name)):
                os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))

            # copy package from volatile drive, extract contents
            os.mkdir('{}/packages_temp/{}'.format(working_dir, dir_name))
            os.system('cp {}/npm-packages/{}/*.tgz {}/packages_temp/{}'.format(volatile_dir, dir_name, working_dir, dir_name))
            os.system('tar zxf {}/packages_temp/{}/*.tgz -C {}/packages_temp/{} > /dev/null 2>&1'.format(working_dir, dir_name, working_dir, dir_name))

            # get a list of all javascript files
            os.system('chmod -R 777 {}/packages_temp/{}'.format(working_dir, dir_name))
            os.system('find {}/packages_temp/{} -type f -name "*.js" >> {}/packages_temp/{}/js_files'.format(working_dir, dir_name, working_dir, dir_name))
            js_files = open('{}/packages_temp/{}/js_files'.format(working_dir, dir_name), 'r').readlines()

            # run tests, record results
            jast_output = jast(js_files, dir_name, thread_id)

            # find package.json
            package_jsons = subprocess.check_output('find {}/packages_temp/{} -type f -name "package.json"'.format(working_dir, dir_name), shell=True).decode('utf8').split()
            package_json_path = min(package_jsons, key=len)

            metadata = json.load(open(package_json_path, 'r'))
            row = metadata['name'] + ',' + metadata['version'] + ','

            row += has_scripts(metadata) + ','
            row += has_install_scripts(metadata) + ','
            row += command_in_install_scripts(metadata, 'curl') + ','
            row += command_in_install_scripts(metadata, 'wget') + ','
            row += command_in_install_scripts(metadata, 'rm') + ','
            row += str(len(js_files)) + ','
            row += jast_output + ','

            called_functions = get_called_functions(js_files)

            row += eval_calls(called_functions) + ','
            row += networking_calls(called_functions) + ','

            row += new_package(metadata) + ','

            typosquatting_result = typosquatting(package_name)

            row += typosquatting_result[0] + ','
            row += typosquatting_result[1]

            log(row)

            if jast_output == 'malicious':
                os.system('mv {}/packages_temp/{}/jast_output {}/malicious_packages/{}_jast_output'.format(working_dir, dir_name, network_dir, dir_name))
                
            os.system('rm -rf {}/packages_temp/{}'.format(working_dir, dir_name))

        except:
            error_file.write('Package: {}\n'.format(package_name))
            error_file.write('{}\n'.format(sys.exc_info()[0]))
            error_file.flush()


def new_package(metadata):

    if 'time' not in metadata:
        return 'no'

    times = metadata['time']    

    earliest_release = ''
    for time in times:
        if time == 'created' or time == 'modified' or time == '0.0.1-security':
            continue

        if earliest_release == '' or times[time] < earliest_release:
            earliest_release = times[time]

    d = datetime.datetime.strptime(earliest_release.split('T')[0], '%Y-%m-%d')

    if (today - d).days < 7:
        return 'yes'
    else:
        return 'no'


def typosquatting(package_name):
    if package_name in popular_packages:
        return ('no', 'N/A')

    candidates = []

    for p in popular_packages:
        if editdistance.eval(package_name, p) == 1:
            candidates.append(p)
			
    if len(candidates) == 0:
        return ('no', 'N/A')
    else:
        return ('yes', '|'.join(candidates))


def has_scripts(metadata):
    return 'yes' if 'scripts' in metadata else 'no'


def has_install_scripts(metadata):
    if 'scripts' not in metadata:
        return 'no'

    for script in install_scripts:
        if script in metadata['scripts']:
            return 'yes'

    return 'no'


def command_in_install_scripts(metadata, command):
    if 'scripts' not in metadata:
        return 'no'

    for script in install_scripts:
        if script in metadata['scripts']:
            parts = metadata['scripts'][script].split()

            for part in parts:
                if part == command:
                    return 'yes'

    return 'no'
    

# Searches for malicious syntax using jast
# param: js_files, list of javascript files to scan
# param: dir_name, where to save jast output file
# param: thread_id, which jast model to use
# return: string, 'malicious' or 'benign'
def jast(js_files, dir_name, thread_id):
    if len(js_files) == 0:
        return 'benign'

    # run jast on all files in js_files list
    for js_file in js_files:
        os.system('python3 {}/jast_models/{}/clustering/classifier.py --v 5 --th 0.1 --m {}/jast_models/{}/Classification/model --f "{}" >> {}/packages_temp/{}/jast_output'.format(working_dir, thread_id, working_dir, thread_id, js_file[:-1], working_dir, dir_name))

    # get number of files classified as malicious
    result = subprocess.check_output('grep ": malicious" {}/packages_temp/{}/jast_output | wc -l'.format(working_dir, dir_name), shell=True)
    n_malicious = int(result.decode('utf8'))

    if n_malicious == 0:
        return 'benign'
    else:
        return 'malicious'


def eval_calls(called_functions):
    if 'eval' in called_functions:
        return 'yes'
    else:
        return 'no'


def networking_calls(called_functions):
    for f in networking_functions:
        if f in called_functions:
            return 'yes'
    return 'no'


if __name__ == '__main__':
    init()
    main()
