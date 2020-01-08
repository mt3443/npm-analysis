import os
import sys

node = sys.argv[1]
os.system('mkdir -p /dev/shm/npm/typosquatting')
os.system('mkdir /dev/shm/npm/data')
os.system('cp _all_docs.json typosquatting.js scan_all_packages.js /dev/shm/npm/typosquatting')
os.system('cp ../data/popular_packages.txt /dev/shm/npm/data')
os.system('node scan_all_packages.js {}'.format(node))
os.system('mv /dev/shm/npm/typosquatting/typosquatting_positives.csv /users/m139t745/npm-analysis/typosquatting/output/positive/{}'.format(node))
os.system('mv /dev/shm/npm/typosquatting/typosquatting_negatives.csv /users/m139t745/npm-analysis/typosquatting/output/negative/{}'.format(node))
os.system('rm -rf /dev/shm/npm')
