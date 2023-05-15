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
