import os
import re
import time

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

if not os.path.isdir('errors'):
    os.mkdir('errors')
else:
    os.system('rm -rf errors/*')

if not os.path.isdir('output'):
    os.mkdir('output')
else:
    os.system('rm -rf output/*')

if not os.path.isdir('malicious_packages'):
    os.mkdir('malicious_packages')
else:
    os.system('rm -rf malicious_pacakges/*')

# start server
os.system('srun -N1 -n 1 -c 1 -w g016 python3 npm_server.py &')

# wait for server to initialize
time.sleep(60)

# start clients
for node in nodes_cores:
    os.system('srun -N 1 -n 1 -c {} -w {} python3 npm_client.py {} &'.format(nodes_cores[node], node, node))

print('Job started')
