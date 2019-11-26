import os
import re
import sys
import requests

print('Getting node info...', flush=True)
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

print('Getting package names...', flush=True)
#all_packages_request = requests.get('https://skimdb.npmjs.com/_all_docs')

#if all_packages_request.status_code != 200:
    #print('Error: status code {} returned for all packages request'.format(all_packages_request.status_code))
    #exit()

import json

all_packages_rows = json.load(open('_all_docs.json', 'r'))['rows']
all_packages = [x['id'] for x in all_packages_rows]

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

if not os.path.isdir('package_names'):
    os.mkdir('package_names')

if not os.path.isdir('errors'):
    os.mkdir('errors')

if not os.path.isdir('popular_packages'):
    os.mkdir('popular_packages')

packages_per_node = int(len(all_packages) / (len(nodes_cores) + 1))

all_chunks = chunks(all_packages, packages_per_node)

# start clients
for node in nodes_cores:
    f = open('package_names/{}'.format(node), 'w')
    current_chunk = next(all_chunks)

    for package_name in current_chunk:
        f.write('{}\n'.format(package_name))

    f.close()

    os.system('srun -N 1 -n 1 -c 1 -w {} python3 downloads_getter.py {} &'.format(node, node))

print('Job started')
