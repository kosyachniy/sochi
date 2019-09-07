import json

from mongodb import db


# Размещение

db['apartments'].remove()

with open('apartments.json', 'r') as file:
	apartments = json.loads(file.read())

for apartment in apartments:
	db['apartments'].insert_one(apartment)


# Пользователи

db['users'].remove()

with open('users.json', 'r') as file:
	users = json.loads(file.read())

for user in users:
	db['users'].insert_one(user)