import re
import sys

# pass in list of js file names
js_files = open(sys.argv[1], 'r').readlines()
required_modules = set()

for js_file in js_files:
	current_file = open(js_file[:-1], 'r').read()
	modules = re.findall(r'require\s*\(\s*[\'|\"](.*?)[\'|\"]\s*\)', current_file)

	for module in modules:
		if module not in required_modules:
			required_modules.add(module)

print(required_modules)