## Запрос
```
{
	lat: Широта (float),
	lng: Долгота (float),
	radius: Радиус (float),
}
```

## Ответ
```
{
	id: ID апартаментов (int),
	name: Название (str),
	description: Описание (str),
	photos: [Картинки (str)],
	price: Цена (int),
	rating: Рейтинг (float),
	location: (Широта (float), Долгота (float)),

	user: {
		id: ID пользователя (int),
		name: Имя (str),
		surname: Фамилия (str),
		tel: Телефон (int),
	},


	entertainment: [{
		name: Название (str),
		location: (Широта (float), Долгота (float)),
		photos: [Картинки (str)],
	}],
}
```