import sys
import json

# pass in path to a package.json file

package_json = json.load(open(sys.argv[1], 'r'))

if 'scripts' not in package_json:
	print('No scripts found.')
	exit(0)

dangerous_commands = [
	'curl',
	'wget'
]

scripts = package_json['scripts']
for script in scripts:
	script_parts = scripts[script].split()

	for script_part in script_parts:
		if script_part.lower() in dangerous_commands:
			print('WARNING: {} used in {} script'.format(script_part, script))
			break