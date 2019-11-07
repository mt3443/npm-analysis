import os

files = open('benign_files', 'r').readlines()

for i in range(len(files)):
	os.system('cp -r {} jast_training/benign/{}'.format(files[i][:-1], i))
