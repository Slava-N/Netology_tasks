#Можно ли собрать библиотеку из рецептов по разделам:
# закуски, 2-е, десерты.
# Потом создать функцию которая будет выводить список и количество продуктов при
# выборе 1,2,3 блюда на _____ персон. В итоге вывести на печать список покупок.
import json, yaml
from pprint import pprint

# выбрать формат
format_recipe = input("Какой формат рецепта выбрать?\njson или yaml\n")
if format_recipe == 'yaml':
    recipe_name = 'recipe_dump.yaml'
else:
    recipe_name = 'recipe_dump.json'
print('Вы выбрали формат {0}, будет использован файл {1} '.format(format_recipe, recipe_name))

with open(recipe_name, encoding='utf-8') as document:
    if format_recipe == 'yaml':
        menu = yaml.load(document)
    else:
        menu = json.load(document)
    # pprint(menu)
    print('В нашем меню представлены следующие блюда: \n {}'.format(list(menu.keys())))

def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dishes[dish]:
            new_shop_item = dict(ingridient)
            # пересчитали ингрединты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count[dish]
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))

def create_shop_list(people_count, *order):
    # получить блюда из кулинарной книги
    dishes = {}
    people_count_dishes = {}
    for dish in order:
        if dish in dishes: people_count_dishes[dish] = people_count_dishes[dish] + people_count
        else:
            if dish in menu:
                dishes[dish] = menu[dish]
                people_count_dishes[dish] = people_count
            else:
                print('Блюдо "{}" закончилось'.format(dish))
    print('Мы приготовим Вам: {0}'.format(people_count_dishes), sep='\n')
    #заполнили список покупок
    shop_list = get_shop_list_by_dishes(dishes, people_count_dishes)
    # Вывести список покупок
    print('Список покупок: ')
    print_shop_list(shop_list)

print('Выберите первое блюдо: ')
first_dish = input()
print('Выберите второе блюдо: ')
second_dish = input()
print('Выберите третье блюдо: ')
third_dish = input()
print('На сколько человек?')
people_count = int(input())
create_shop_list(people_count, first_dish, second_dish, third_dish)
