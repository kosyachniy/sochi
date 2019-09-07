from mongodb import db


# Размещение

db['apartments'].remove()

apartments = [
	{
		"name": "Бабушка на час",
		"description": "Побывай там, где никогда не был",
		"location": [44.079315, 39.118204],
		"user": 1,
		"price": 500,
		"entertainment": [{
			"name": "Подоить корову",
			"location": [44.079, 39.12]
		}, {
			"name": "Снять сено",
			"location": [44.0795, 39.119]
		}],
		"photos": [
			"https://hdwallsbox.com/wallpapers/l/1920x1200/61/winter-trees-forest-abandoned-cottage-1920x1200-60209.jpg",
			"https://s1.1zoom.ru/big3/705/364849-svetik.jpg"
		]
	},
	{
		"name": "Город для лохов, деревня для пацанов",
		"description": "Настоящая суровая деревня не для слабонервных",
		"location": [44.075, 39.11],
		"user": 2,
		"price": 700,
		"entertainment": {
			"name": "Родить цыплёнков",
			"location": [44.0754, 39.111],
		},
		"photos": [
			"https://otvet.imgsmail.ru/download/197607421_3ecceffc1ec779ea0acfbc2840b41691_800.jpg"
		]
	}
]

for apartment in apartments:
	db['apartments'].insert_one(apartment)


# Пользователи

db['users'].remove()

users = [
	{
		"id": 1,
		"name": "Елизавета",
		"surname": "Деревенская",
		"tel": 79998087533,
	},
	{
		"id": 2,
		"name": "Дарья",
		"surname": "Загородняя",
		"tel": 78127501010,
	}
]

for user in users:
	db['users'].insert_one(user)