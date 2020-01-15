import json
import os
import re
import random
import pandas as pd
import requests

# get all packages
print('Downloading all docs', flush=True)
all_packages_json = requests.get('https://replicate.npmjs.com/_all_docs').json()
all_packages = [x['id'] for x in all_packages_json['rows']]
del all_packages_json

download_counts = pd.read_csv('data/downloads.csv')
recorded_packages = set(download_counts.package_name.values)

print('Getting packages to download', flush=True)
all_packages_set = set(all_packages)
for recorded_package in recorded_packages:
    if recorded_package in all_packages_set:
        all_packages_set.remove(recorded_package)
all_packages = list(all_packages_set)

os.system('scontrol show node > node_info')
node_info = open('node_info', 'r').readlines()

all_nodes = []

current_node = ''

for line in node_info:
    if line == '\n':
        all_nodes.append(current_node)
        current_node = ''
    else:
        current_node += line

os.system('rm node_info')

unused_nodes = []

for node in all_nodes:
    if 'CPUAlloc=0' in node and 'NodeName=g' not in node and 'NodeName=m' not in node and 'amd' not in node:
        unused_nodes.append(node)

del all_nodes

total_cores = 0
nodes_cores = {}

for node in unused_nodes:
    name = re.findall(r'NodeName=(\S+)', node)[0]
    n_cores = re.findall(r'CPUTot=(\d+)', node)[0]
    nodes_cores[name] = n_cores
    total_cores += int(n_cores)

if not os.path.isdir('data/download_counts'):
    os.mkdir('data/download_counts')
else:
    os.system('rm -rf data/download_counts/*')

os.mkdir('data/download_counts/success')
os.mkdir('data/download_counts/fail')

if not os.path.isdir('download_package_names'):
    os.mkdir('download_package_names')
else:
    os.system('rm -rf download_package_names/*')

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

all_chunks = chunks(all_packages, int(len(all_packages) / len(nodes_cores)) + 1)

# assign packages
for node in nodes_cores:
	current_chunk = next(all_chunks)
	f = open('download_package_names/{}'.format(node), 'w')
	for p in current_chunk:
		f.write('{}\n'.format(p))
	f.close()

# start clients
for node in nodes_cores:
    os.system('srun -N 1 -n 1 -c {} -w {} python3 download_count_getter.py {} &'.format(nodes_cores[node], node, node))

print('Job started')
