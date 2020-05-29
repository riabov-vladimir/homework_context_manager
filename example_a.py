from pprint import pprint


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


#pprint(txt_to_dict('recipes.txt')) #         <<<<<<<---------- раскомментировать для проверки кода