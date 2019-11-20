import requests
import os
import threading

n_nodes = 64

all_packages_request = requests.get('https://replicate.npmjs.com/_all_docs')

if all_packages_request.status_code != 200:
	print('ERROR: status code {} returned for package list request'.format(all_packages_request.status_code))
	exit(1)

all_package_names = [x[:-1] for x in all_packages]

del all_packages

def download_packages(packages):
	for package_name in packages:
		dir_name = package_name.replace('/', '~')

		try:

			metadata_request = requests.get('https://registry.npmjs.org/{}'.format(package_name))

			if metadata_request.status_code != 200:
				print('ERROR: status code {} returned for {} metadata'.format(metadata_request.status_code, package_name))
				continue

			metadata = metadata_request.json()
			latest_version = metadata['dist-tags']['latest']
			source_code_url = metadata['versions'][latest_version]['dist']['tarball']

			source_code_request = requests.get(source_code_url)

			if source_code_request.status_code != 200:
				print('ERROR: status code {} returned for {} source code'.format(source_code_request, package_name))
				continue

			if not os.path.exists('{}/{}'.format(storage_dir, dir_name)):
				os.mkdir('{}/{}'.format(storage_dir, dir_name))

			source_code_path = '{}/{}/{}.tgz'.format(storage_dir, dir_name, latest_version)
			with open(source_code_path, 'wb') as f:
				f.write(source_code_request.content)

		except:
			print('ERROR: unhandled exception when processing {}'.format(package_name))

def chunks(l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]

threads = []
all_chunks = chunks(all_package_names, int(len(all_package_names) / n_threads) + 1)

for i in range(n_threads):
	chunk = next(all_chunks)
	t = threading.Thread(target=download_packages, args=(chunk,))
	t.start()
	threads.append(t)

for t in threads:
	t.join()
