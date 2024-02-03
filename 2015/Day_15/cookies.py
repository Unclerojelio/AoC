import time
import re
from itertools import permutations

def do_tests():
    lines = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''
    lines = lines.splitlines()
    ingredients = parse_file(lines)
    ans1, ans2 = solve(ingredients)

    #assert ans1 == 62842880
    return True

def parse_file(lines):
    ingredients = {}
    for line in lines:
        name, line = line.split(':')
        capacity, durability, flavor, texture, calories = line.split(',')
        _, capacity = capacity.split()
        _, durability = durability.split()
        _, flavor = flavor.split()
        _, texture = texture.split()
        _, calories = calories.split()
        ingredients[name] = [int(capacity), int(durability), int(flavor), int(texture), int(calories)]
    return ingredients


def solve(ingredients):
    for ingredient in ingredients:
        print(ingredient, ingredients[ingredient])
    ans1 = 0
    ans2 = 0

    return ans1, ans2

def main():
    start_time = time.time()

    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ingredients = parse_file(lines)
    ans1, ans2 = solve(ingredients)
    
    # assert ans1 == 2660
    # assert ans2 == 1256
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()