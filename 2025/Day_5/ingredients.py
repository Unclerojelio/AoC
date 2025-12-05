# usage: python3 ingredients.py < input.txt

import time
from collections import defaultdict

def do_tests():
    lines = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
    grid = parse(lines)
    ans1, ans2 = solve(grid)
    assert ans1 == 3
    assert ans2 == 0
    return True

def parse(lines):
    grid = [list(line) for line in lines.strip().splitlines()]
    return grid

def solve(grid):
    ans1 = 0
    ans2 = 0
    removes = do_pass(grid)
    ans1 = len(removes)
    ans2 = len(removes)
    for remove in removes:
        grid[remove[1]][remove[0]] = "."
    while True:
        removes = do_pass(grid)
        ans2 += len(removes)
        if len(removes) == 0:
            break
        for remove in removes:
            grid[remove[1]][remove[0]] = "."
    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read()
    banks = parse(lines)
    ans1, ans2 = solve(banks)
    assert ans1 == 0
    assert ans2 == 0
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
