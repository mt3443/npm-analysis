import requests
import sys

n_downloads = int(sys.argv[1])
all_packages_request = requests.get('https://replicate.npmjs.com/_all_docs')

if all_packages_request.status_code != 200:
	print('Error: all packages request returned status code {}'.format(all_packages_request.status_code))
	exit()

all_packages_rows = all_packages_request.json()['rows']
all_packages = [x['id'] for x in all_packages_rows]

downloads_endpoint = 'https://api.npmjs.org/downloads/point/last-week'

popular_packages = open('packages_with_{}_downloads.txt'.format(n_downloads), 'w')

for package_name in all_packages:
	downloads_request = requests.get('{}/{}'.format(downloads_endpoint, package_name))

	if downloads_request.status_code != 200:
		print('Error: downloads request for {} returned status code {}'.format(package_name, downloads_request.status_code))
		continue

	downloads = downloads_request.json()['downloads']

	if downloads > n_downloads:
		popular_packages.write('{}\n'.format(package_name))

popular_packages.close()