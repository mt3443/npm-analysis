import json
import os
import re
import random

# get all packages
all_packages_json = json.load(open('_all_docs.json', encoding='utf8'))['rows']
all_packages = [x['id'] for x in all_packages_json]
random.shuffle(all_packages)
del all_packages_json

# remove package names that have already been analyzed
if os.path.exists('transitive_output1'):
    all_packages_set = set(all_packages)
    log_dirs = ['transitive_output1/negative', 'transitive_output1/positive']
    
    for d in log_dirs:
        log_files = os.listdir(d)
        for l in log_files:
            packages = open(os.path.join(d, l)).read().splitlines()
            for p in packages:
                if len(p.split(',')) > 4:
                    continue
                x = p.split(',')[0]
                if x in all_packages_set:
                    all_packages_set.remove(x)
    
    all_packages = list(all_packages_set)
    del all_packages_set

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
total_packages = len(all_packages)
nodes_cores = {}

for node in unused_nodes:
    name = re.findall(r'NodeName=(\S+)', node)[0]
    n_cores = re.findall(r'CPUTot=(\d+)', node)[0]
    nodes_cores[name] = n_cores
    total_cores += int(n_cores)

if not os.path.isdir('transitive_output'):
    os.mkdir('transitive_output')
else:
    os.system('rm -rf transitive_output/*')

os.mkdir('transitive_output/positive')
os.mkdir('transitive_output/negative')

if not os.path.isdir('transitive_package_names'):
    os.mkdir('transitive_package_names')
else:
    os.system('rm -rf transitive_package_names/*')

packages_per_core = int(total_packages / total_cores) + 1

# assign packages
for node in nodes_cores:
    packages_for_this_node = packages_per_core * int(nodes_cores[node])
    f = open('transitive_package_names/{}'.format(node), 'w')
    for _ in range(packages_for_this_node):
        if (len(all_packages) == 0):
            break
        f.write('{}\n'.format(all_packages.pop()))
    f.close()

# start clients
for node in nodes_cores:
    os.system('srun -N 1 -n 1 -c {} -w {} python3 start_transitive.py {} {} &'.format(nodes_cores[node], node, node, nodes_cores[node]))

print('Job started')
