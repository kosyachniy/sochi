## БД
``` apartments ```
```
{
	id: ID апартаментов,
	name: Название,
	description: Описание,
	rating: Рейтинг,
	location: (Широта, Долгота),
	user: ID пользователя,
	price: Цена,
	entertainment: [{
		name: Название,
		location: (Широта, Долгота),
		photos: [Картинки],
	}],
	photos: [Картинки],
}
```

``` users ```
```
{
	id: ID пользователя,
	name: Имя,
	surname: Фамилия,
	tel: Телефон,
}
```