from pprint import pprint

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
