from subprocess import check_output, CalledProcessError, STDOUT

def get_called_functions(js_files):
    all_functions = set()

    for f in js_files:
        try:
            result = check_output('node find_functions.js {}'.format(f[:-1]), shell=True, stderr=STDOUT)

            functions = set(result.decode('utf8').split())
            all_functions = all_functions.union(functions)
        
        except CalledProcessError as e:
            continue

    return all_functions
