import fileinput
import itertools
import re

class Food(object):
    def __init__(self, ingredient_list, allergen_list):
        self.ingredients = [ingredient.strip() for ingredient in ingredient_list.split()]
        self.allergens = [allergen.strip() for allergen in allergen_list.split(',')]

def read_foods():
    food_info = re.compile('(?P<ingredient_list>[^(]+)\(contains(?P<allergen_list>.+)\)$')
    foods = []
    for line in fileinput.input():
        if m:= food_info.match(line):
            foods.append(Food(m.group('ingredient_list'), m.group('allergen_list')))
    return foods

def analyze(foods):
    ingredients_lists = [food.ingredients for food in foods]
    all_ingredients = set(itertools.chain(*ingredients_lists))
    all_allergens = set(itertools.chain(*[food.allergens for food in foods]))

    possible_ingredients = dict()
    for allergen in all_allergens:
        possible_foods = [food for food in foods if allergen in food.allergens]
        ingredients = all_ingredients.copy()
        for food in possible_foods:
            ingredients.intersection_update(food.ingredients)
        possible_ingredients[allergen] = ingredients

    suspect_ingredients = set()
    for food in foods:
        suspect_ingredients.update(*[possible_ingredients[allergen] for allergen in food.allergens])

    safe_ingredients = all_ingredients.difference(suspect_ingredients)
    all_ingredients = list(itertools.chain(*ingredients_lists))
    return sum(all_ingredients.count(ingredient) for ingredient in safe_ingredients)

def main():
    foods = read_foods()
    print(analyze(foods))

if __name__ == "__main__":
    main()
