import os
import sys
import ast
import subprocess

node = sys.argv[1]
os.system('rm -rf /dev/shm/npm')
os.system('mkdir -p /dev/shm/npm/transitive')
os.system('mkdir /dev/shm/npm/data')
os.system('cp ../data/typosquatting_candidates.txt /dev/shm/npm/data')

positive_log = open('/dev/shm/npm/transitive/positive', 'w')
negative_log = open('/dev/shm/npm/transitive/negative', 'w')

typosquatting_candidates = set(open('/dev/shm/npm/data/typosquatting_candidates.txt').read().splitlines())

machine_packages = open('/users/m139t745/npm-analysis/typosquatting/transitive_package_names/{}'.format(node)).read().splitlines()

for package_name in machine_packages:

    if package_name in typosquatting_candidates:
        positive_log.write('{}\n'.format(package_name))
        continue

    result = subprocess.check_output('npm-remote-ls -n {} -f -d false'.format(package_name), shell=True).decode('utf8')

    # remove any error text
    bracket_index = result.find('[')
    result = result[bracket_index:]

    try:
        typosquatting = False
        raw_dependencies = ast.literal_eval(result)
        for dependency in raw_dependencies:
            if dependency[0] == '@':
                at_index = dependency.find('@', 1)
                clean_dependency = dependency[:at_index]
            else:
                clean_dependency = dependency.split('@')[0]

            if clean_dependency in typosquatting_candidates:
                typosquatting = True
                positive_log.write('{}\n'.format(package_name))
                positive_log.flush()
                break

        if not typosquatting:
            negative_log.write('{}\n'.format(package_name))
            negative_log.flush()

    except:
        negative_log.write('{}\n'.format(package_name))
        negative_log.flush()

positive_log.close()
negative_log.close()

os.system('mv /dev/shm/npm/transitive/positive /users/m139t745/npm-analysis/typosquatting/transitive_output/positive/{}'.format(node))
os.system('mv /dev/shm/npm/transitive/negative /users/m139t745/npm-analysis/typosquatting/transitive_output/negative/{}'.format(node))
os.system('rm -rf /dev/shm/npm')
