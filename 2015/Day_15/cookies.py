import time
import re
from itertools import permutations

def partitionfunc(n,k,l=1):
    '''n is the integer to partition, k is the length of partitions, l is the min partition element size'''
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range(l,n+1):
        for result in partitionfunc(n-i,k-1,i):
            yield (i,)+result

def get_partitions(n, k):
    #return [(44, 56)]
    return

def get_score(ingredients, partition):
    table = []
    for i, ingredient in enumerate(ingredients):
        sums = []
        for property in ingredients[ingredient]:    
            sums.append(property * partition[i])
        table.append(sums)
    score = 1
    for j in range(len(table[0])-1): # properties
        temp = 0
        for i in range(len(table)): # ingredients
            temp += table[i][j]
        temp = max(temp, 0)
        score *= temp
    return score


def do_tests():
    lines = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''
    lines = lines.splitlines()
    ingredients = parse_file(lines)
    partitions = [(44, 56)]
    ans1, ans2 = solve(ingredients, partitions)

    assert ans1 == 62842880
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


def solve(ingredients, partitions):
    ans1 = 0
    for partition in partitions:
        score = get_score(ingredients, partition)
        ans1 = max(ans1, score)
    
    ans1 = score
    ans2 = 0

    return ans1, ans2

def main():
    start_time = time.time()

    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ingredients = parse_file(lines)
    partitions = get_partitions(100, len(ingredients))
    ans1, ans2 = solve(ingredients, partitions)
    
    # assert ans1 == 2660
    # assert ans2 == 1256
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()