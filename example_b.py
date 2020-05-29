from example_a import txt_to_dict
from pprint import pprint

cook_book = txt_to_dict('recipes.txt')


def get_shop_list_by_dishes(dishes=('Фахитос', 'Омлет'), person_count=5):
	'''Функция, принимающая в качестве аргументов блюдо (или несколко блюд) и количество персон. Чтобы не морочиться
	с input(), задал значения по умолчанию, в которых как раз прорабатывается вариант с повторяющимися ингредиентами'''
	target = {}
	# сначала собираю новый словарь
	for dish in dishes:  # первая итерация по списку блюд принемаемому в качестве аргумента функции
		if dish in cook_book.keys():   # отсеиваю обработку блюд, не входящих в список dishes
			for temp in cook_book[dish]: # распаковываю словари ингредиентов по каждому блюду
				if temp['ingredient_name'] not in target.keys():
					target.setdefault(temp.pop('ingredient_name'), temp)
				else:
					target[temp['ingredient_name']]['quantity'] += target[temp['ingredient_name']]['quantity']

	for value in target.values():     # затем умножаю все показатели "quantity" на значение переменной person_count
		value['quantity'] = value['quantity'] * person_count

	return target


pprint(get_shop_list_by_dishes())
