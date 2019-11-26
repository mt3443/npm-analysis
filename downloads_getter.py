import requests
import sys

node_name = sys.argv[1]

all_packages_request = requests.get('https://replicate.npmjs.com/_all_docs')

all_packages = open('package_names/{}'.format(node_name), 'r').readlines()

downloads_endpoint = 'https://api.npmjs.org/downloads/point/last-week'

popular_packages = open('/users/m139t745/npm-analysis/popular_packages/{}'.format(node_name), 'w')
errors = open('/users/m139t745/npm-analysis/errors/{}'.format(node_name), 'w')

for package in all_packages:
    package_name = package[:-1]
    downloads_request = requests.get('{}/{}'.format(downloads_endpoint, package_name))

    if downloads_request.status_code != 200:
        errors.write('Error: downloads request for {} returned status code {}\n'.format(package_name, downloads_request.status_code))
        continue

    downloads = downloads_request.json()['downloads']

    popular_packages.write('{},{}\n'.format(package_name, downloads))

popular_packages.close()
errors.close()
