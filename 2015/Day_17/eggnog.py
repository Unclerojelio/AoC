import time
import re
from itertools import permutations


def parse_file(lines):
  containers = [int(line) for line in lines]
  return containers

def solve(containers, amount):
    ans1 = 0
    ans2 = 0
    return ans1, ans2

def do_tests():
    lines = '''20
    15
    10
    5
    5'''
    lines = lines.splitlines()
    containers = parse_file(lines)
    ans1 = solve(containers, 25)
    #ans2 = solve(ingredients, partitions, True)

    # assert ans1 == 62842880
    # assert ans2 == 57600000
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    containers = parse_file(open(0).read().splitlines())
    ans1, ans2 = solve(containers, 150)
    
    # assert ans1 == 103
    # assert ans2 == 405
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()