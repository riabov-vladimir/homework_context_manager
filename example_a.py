def ingredient(ing_line):
	"""Функция, которая принимает строку с ингридиентами из файла и возвращает словарь"""
	ing_line = ing_line.split(' | ')
	dict = {'ingredient_name': ing_line[0], 'quantity': int(ing_line[1]), 'measure': ing_line[2].strip()}
	return dict


def txt_to_dict(file_name):
	'''Основная функция, конвертирующая наш файл в словарь. Принимает в качестве аргумента имя файла'''
	dict = {} # ключи - названия блюд, значения - списки из словарей с игредиентами
	with open(file_name, 'r') as file:
		for line in file:
			if len(line) == 2: # отсеиваю строки с кол-вом ингредиентов
				pass
			elif len(line) == 1: # отсеиваю пустые строки
				pass
			elif '|' not in line: # строки с текстом, но без знака "|" содержат названия блюд
				temp = line.strip()
			elif '|' in line:
				dict.setdefault(temp, [])
				dict[temp].append(ingredient(line))
	return dict

def get_shop_list_by_dishes(cook_book, dishes=('Фахитос', 'Омлет'), person_count=5):
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
