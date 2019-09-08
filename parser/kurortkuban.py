import time
import json
import random

import requests
from bs4 import BeautifulSoup


LINK = 'https://min.kurortkuban.ru/'
url = LINK + 'agroturizm/objects/?mo='

data = []

CATEGORIES = (
	'озеро', 'ранчо', 'ферма', 'фирма', 'парк', 'винодельня',
	'подворье', 'грибной', 'чая', 'путь', 'компания', 'зоопарк',
)

# Получаем html-код

html = requests.get(url).text

# Парсинг

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('div', {'class': 'objects-wrapper'}) # container-fluid
articles = soup.find_all('div', {'class': 'item'})

for article in articles:
	try:
		name = article.find('div', {'class': 'title'}).text
		src = article.a.get('href')
		img = article.find('div', {'class': 'img'}).get('style')
		description = article.find('div', {'class': 'txt'}).text
	except:
		continue

	def getGeo():
		while True:
			x = random.uniform(43.455421, 45.994610)
			y = random.uniform(37.156351, 41.372443)
			fl = lambda x, y: -1.050935 * x + 0.965895 * y + 11.475324
			ft = lambda x, y: 2.66464 * x + 1.877251 * y - 194.694532
			fr = lambda x, y: 1.046292 * x - 0.6491 * y - 19.693632
			fb = lambda x, y: -2.669284 * x - 1.560456 * y + 178.5643

			if fl(x, y) > 0 and fr(x, y) > 0 and ft(x, y) < 0 and fb(x, y) < 0:
				return x, y

	# !!! Entertainment
	if False: # any(i in name.lower() for i in CATEGORIES):
		if len(data):
			data[random.randint(0, len(data)-1)]['entertainment'].append({
				'name': name.strip(),
				'location': getGeo(),
				'photos': [LINK + img[23:-1]],
			})

		continue

	req = {
		'id': len(data) + 1,
		'name': name.strip(),
		'link': LINK + src,
		'photos': [LINK + img[23:-1]],
		'description': description.strip(),

		'rating': random.randint(40, 100) / 10,
		'price': random.randint(300, 2000),
		'location': getGeo(),
		'user': random.randint(1, 5),

		"entertainment": [],
	}

	data.append(req)

	# print(data)

with open('../re/data/real/apartments.json', 'w') as file:
	print(json.dumps(data, ensure_ascii=False, indent='\t'), file=file)