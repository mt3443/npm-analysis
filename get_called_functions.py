import subprocess

def get_called_functions(js_files):
    all_functions = set()

    for f in js_files:
        result = subprocess.check_output('node find_functions.js {}'.format(f[:-1]), shell=True)
        functions = set(result.decode('utf8').split())
        all_functions = all_functions.union(functions)

    return list(all_functions)