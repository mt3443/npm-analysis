import os
import re
import requests
import random

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
	if 'CPUAlloc=0' in node and 'NodeName=g' not in node:
		unused_nodes.append(node)

del all_nodes

total_cores = 0
nodes_cores = {}

for node in unused_nodes:
	name = re.findall(r'NodeName=(\S+)', node)[0]
	n_cores = re.findall(r'CPUTot=(\d+)', node)[0]
	nodes_cores[name] = n_cores
	total_cores += int(n_cores)

# get all package names
print('Getting package names...', flush=True)
all_packages_request = requests.get('https://replicate.npmjs.com/_all_docs')

if all_packages_request.status_code != 200:
	print('Error: All packages request returned status code', all_packages_request.status_code)
	exit()

all_docs = all_packages_request.json()
total_packages = all_docs['total_rows']
all_package_names = [x['id'] for x in all_docs['rows']]
random.shuffle(all_package_names)

del all_docs

packages_dir = '/volatile/m139t745/npm-packages'

if not os.path.exists(packages_dir):
	os.mkdir(packages_dir)

# divide packages equally among number of nodes
packages_per_node = int(total_packages / len(nodes_cores)) + 1

# prep package_names directory
# assign packages to nodes
print('Assigning packages to nodes...', flush=True)
os.system('rm -rf package_names')
os.mkdir('package_names')

for node in nodes_cores:
	f = open('package_names/{}'.format(node), 'w')
	for p in range(packages_per_node):
		f.write('{}\n'.format(all_package_names.pop()))
		if len(all_package_names) == 0:
			break
	f.close()

for node in nodes_cores:
    os.system('srun -N1 -n1 -c4 -w {} python3 package_downloader.py {} 4 &\n'.format(node, node))

print('Job started')
