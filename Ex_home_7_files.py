from pprint import pprint
import os

print('\nЗадача №1\n')

with open('dish_recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for i in range(ingredients_count):
            dish = file.readline()
            ingredient, quantity, measure = dish.strip().split(' | ')
            ingredient_dict = {
                'ingredient_name': ingredient,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(ingredient_dict)
        file.readline()
        cook_book[dishes] = ingredients

    pprint(cook_book, sort_dicts=False)

print('\nЗадача №2\n')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name in dishes:
        for ingredient in cook_book[dish_name]:
            if ingredient['ingredient_name'] not in shop_list:
                quantity_dict = {
                    'measure': ingredient['measure'],
                    'quantity': int(ingredient['quantity']) * person_count

                }
                shop_list[ingredient['ingredient_name']] = quantity_dict
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count

    pprint(shop_list, sort_dicts=False)
    print()


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 3)


current = os.getcwd()

with open(os.path.join(current, '1.txt'), encoding='utf-8') as file_1, open(os.path.join(current, '2.txt'),
     encoding='utf-8') as file_2, open(os.path.join(current, '3.txt'), encoding='utf-8') as file_3, \
     open(os.path.join(current, 'new.txt'), 'w', encoding='utf-8') as new_file:
    dict_files = {
        file_1: [len(file_1.readlines()), '1.txt'],
        file_2: [len(file_2.readlines()), '2.txt'],
        file_3: [len(file_3.readlines()), '3.txt']
    }

    sort_dict_files = dict(sorted(dict_files.items(), key=lambda item: item[1][0]))

    file_1.seek(0)
    file_2.seek(0)
    file_3.seek(0)

    for keys, values in sort_dict_files.items():
        new_file.writelines(f'{values[1]}\n')
        new_file.writelines(f'{values[0]}\n')
        for line in keys.readlines():
            new_file.writelines(f'{line}')
        new_file.writelines('\n')

    pprint(sort_dict_files, sort_dicts=False)
