import os
import re

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
packages_dir = '/volatile/m139t745/npm-packages'
all_packages = [f for f in os.listdir(packages_dir) if os.path.isdir(os.path.join(packages_dir, f))]
total_packages = len(all_packages)

# divide packages equally among number of cores
packages_per_core = int(total_packages / total_cores) + 1

# prep package_names directory
# assign packages to cores
os.system('rm -rf package_names')
os.mkdir('package_names')

for node in nodes_cores:
	f = open('package_names/{}'.format(node), 'w')
	for p in range(nodes_cores[node] * packages_per_core):
		f.write('{}\n'.format(all_packages.pop()))
	f.close()

for node in nodes_cores:
	os.system('srun -N 1 -n {} -c 1 -w {} --exclusive python3 test_model.py {} {} &'.format(nodes_cores[node], node, node, nodes_cores[node]))

os.system('wait')
