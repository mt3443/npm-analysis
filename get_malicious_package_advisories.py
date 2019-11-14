from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.npmjs.com/advisories?perPage=9999')
soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.find_all('tr')[1:]

f = open('malicious_packages.csv', 'w')
f.write('package_name,url\n')

for row in rows:
	if row.td.a.text == 'Malicious Package':
		f.write(row.td.find_all('div')[1].text + ',' + 'https://www.npmjs.com{}'.format(row.td.a['href']) + '\n')