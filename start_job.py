import os
import re

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

# get all package names
print('Getting package names...', flush=True)
packages_dir = '/volatile/m139t745/npm-packages'
all_packages = [f for f in os.listdir(packages_dir)]
total_packages = len(all_packages)

# divide packages equally among number of cores
packages_per_core = int(total_packages / total_cores) + 1

# prep package_names directory
# assign packages to cores
print('Assigning packages to cores...', flush=True)
os.system('rm -rf package_names')
os.mkdir('package_names')

if not os.path.isdir('errors'):
    os.mkdir('errors')

if not os.path.isdir('output'):
    os.mkdir('output')

if not os.path.isdir('malicious_packages'):
    os.mkdir('malicious_packages')

for node in nodes_cores:
    f = open('package_names/{}'.format(node), 'w')
    for p in range(int(nodes_cores[node]) * packages_per_core):
        f.write('{}\n'.format(all_packages.pop()))
        if len(all_packages) == 0:
            break
    f.close()

for node in nodes_cores:
    os.system('srun -N 1 -n 1 -c {} -w {} -e errors/{} python3 scan_packages.py {} {} &'.format(nodes_cores[node], node, node, node, nodes_cores[node]))

print('Job started')
