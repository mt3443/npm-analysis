import re
import json
import requests
import os

# pass in list of js_file names, no new line on the end of each file name
def find_modules(package_name, version):
    try:
        volatile_dir = '/volatile/m139t745/npm-packages'
        local_dir = '/dev/shm/find_modules'

        if not os.path.exists(local_dir):
            os.mkdir(local_dir)

        dir_name = package_name.replace('/', '~')

        os.mkdir('{}/{}'.format(local_dir, dir_name))

        # get specified version of specified package
        if os.path.exists('{}/{}/{}.tgz'.format(volatile_dir, dir_name, version)):
            os.system('cp {}/{}/{}.tgz {}/{}'.format(volatile_dir, dir_name, version, local_dir, dir_name))
        else:
            r = requests.get('https://registry.npmjs.org/{}/-/{}-{}.tgz'.format(package_name, package_name, version))
            if r.status_code != 200:
                print('error: status code {} returned for source code request of package {}'.format(r.status_code, package_name))
                os.system('rm -rf {}/{}'.format(local_dir, dir_name))
                return
            with open('{}/{}/{}.tgz'.format(local_dir, dir_name, version), 'wb') as f:
                f.write(r.content)


        os.system('tar zxf {}/{}/{}.tgz -C {}/{}'.format(local_dir, dir_name, version, local_dir, dir_name))

        # find all js files and package.json
        js_files = []
        package_json_path = ''
        for root, dirs, files in os.walk('{}/{}'.format(local_dir, dir_name)):
            for file in files:
                if file.endswith('.js'):
                    js_files.append(os.path.join(root, file))
                elif file == 'package.json':
                    package_json_path = os.path.join(root, file)

        if package_json_path == '':
            print('error: could not find package.json for {}'.format(package_name))
            os.system('rm -rf {}/{}'.format(local_dir, dir_name))
            return

        required_modules = set()

        package_json = json.load(open(package_json_path, 'r'))
        if 'dependencies' in package_json:
            dependencies = package_json['dependencies']
            for d in list(dependencies.keys()):
                if d not in required_modules:
                    required_modules.add(d)

        for js_file in js_files:
            current_file = open(js_file, 'r').read()
            modules = re.findall(r'require\s*\(\s*[\'|\"](.*?)[\'|\"]\s*\)', current_file)

            for module in modules:
                if module not in required_modules:
                    required_modules.add(module)

        os.system('rm -rf {}/{}'.format(local_dir, dir_name))

        return required_modules
    except: 
        os.system('rm -rf {}/{}'.format(local_dir, dir_name))
        print('error: unhandled exception when processing {} version {}'.format(package_name, version))
        return -1
