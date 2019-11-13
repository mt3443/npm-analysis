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
