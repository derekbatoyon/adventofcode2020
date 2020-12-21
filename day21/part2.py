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

def conflict(list1, list2):
    a_to_i = {a: i for a, i in list2}
    i_to_a = {i: a for a, i in list2}
    for allergen, ingredient in list1:
        if allergen in a_to_i and a_to_i[allergen] != ingredient:
            return True
        if ingredient in i_to_a and i_to_a[ingredient] != allergen:
            return True

def make_guesses(foods, previous_guesses=[], indent=0):
    if foods:
        food = foods[0]
        ingredient_count = len(food.ingredients)
        allergen_count = len(food.allergens)
        for permutation in itertools.permutations(range(ingredient_count), allergen_count):
            guesses = []
            for allergen_index, ingredient_index in enumerate(permutation):
                guesses.append((food.allergens[allergen_index], food.ingredients[ingredient_index]))
            if not conflict(previous_guesses, guesses):
                yield from make_guesses(foods[1:], guesses+previous_guesses, indent+4)
    else:
        yield set(previous_guesses)

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

    for food in foods:
        ingredients = set()
        ingredients.update(*[possible_ingredients[allergen] for allergen in food.allergens])
        food.ingredients = list(ingredients)

    guess = list(make_guesses(foods))
    assert len(guess) == 1

    return ','.join([ingredient for _, ingredient in sorted(guess[0])])

def main():
    foods = read_foods()
    print(analyze(foods))

if __name__ == "__main__":
    main()
