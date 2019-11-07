from find_modules import find_modules
import requests

def find_new_modules(package_name, new_version):
    r = requests.get('https://registry.npmjs.org/{}'.format(package_name))
    if r.status_code != 200:
        print('error: status code {} returned for {} metadata'.format(r.status_code, package_name))
        return
    try:
        metadata = r.json()
        all_times = metadata['time']
        all_times.pop('modified', None)
        all_times.pop('created', None)
        sorted_versions = sorted(all_times.items(), key=lambda kv: kv[1])
        
        old_version = ''

        for i in range(len(sorted_versions)):
            current_version = sorted_versions[i][0]
            if current_version == new_version:
                if i != 0:
                    old_version = sorted_versions[i - 1][0]
                    break

        if old_version == '':
            return find_modules(package_name, new_version)
        
        new_dependencies = find_modules(package_name, new_version)
        old_dependencies = find_modules(package_name, old_version)

        return new_dependencies - old_dependencies

    except:
        print('error: unhandled exception when processing {} version {}'.format(package_name, new_version))
        return -1
