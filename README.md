# Туапсе Camp
## БД
``` apartments ```
```
{
	name: Название,
	description: Описание,
	location: (Широта, Долгота),
	user: ID,
	price: Цена,
	entertainment: {
		name: Название,
		location: (Широта, Долгота),
	},
	photos: [Картинки],
}
```

``` users ```
```
{
	id: ID,
	name: Имя,
	surname: Фамилия,
	tel: Телефон,
}
```