import os
import subprocess
import sys

function_counts = {}

for root, dirs, files in os.walk(sys.argv[1]):
	for f in files:
		if f.endswith('.js'):
			output = subprocess.check_output('node find_functions.js {}'.format(os.path.join(root, f)), shell=True)

			function_names = output.decode('utf8').split()

			for function_name in function_names:
				if function_name in function_counts:
					function_counts[function_name] += 1
				else:
					function_counts[function_name] = 1

out = open('function_counts.csv', 'w')

out.write('function_name,number_of_files_found_in\n')

for key in function_counts:
	out.write('{},{}\n'.format(key, function_counts[key]))

out.close()