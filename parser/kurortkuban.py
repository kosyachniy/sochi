import time
import json
import random

import requests
from bs4 import BeautifulSoup


LINK = 'https://min.kurortkuban.ru/'
url = LINK + 'agroturizm/objects/?mo='

data = []

CATEGORIES = (
	'озеро', 'ранчо', 'ферма', 'агрофирма', 'парк', 'винодельня',
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

	if any(i in name for i in CATEGORIES):
		if len(data):
			data[random.randint(0, len(data)-1)]['entertainment'].append({
				'name': name.strip(),
				'location': (random.uniform(43.951895, 44.191241), random.uniform(38.946721, 39.435738)),
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
		'location': (random.uniform(43.951895, 44.191241), random.uniform(38.946721, 39.435738)),
		'user': random.randint(1, 5),

		"entertainment": [],
	}

	data.append(req)

	# print(data)

with open('../re/data/real/apartments.json', 'w') as file:
	print(json.dumps(data, ensure_ascii=False, indent='\t'), file=file)