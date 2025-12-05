# usage: python3 paper.py < input.txt

import time
from collections import defaultdict

def do_tests():
    lines = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''
    grid = parse(lines)
    ans1, ans2 = solve(grid)
    assert ans1 == 13
    assert ans2 == 43
    return True

def parse(lines):
    grid = [list(line) for line in lines.strip().splitlines()]
    return grid

def do_pass(grid):
    count = 0
    removes = []
    n = len(grid)
    m = len(grid[0])
    for y in range(n):
        for x in range(m):
            if grid[y][x] == '@':
                if x > 0 and y > 0 and grid[y-1][x-1] == '@':
                    count += 1
                if y > 0 and grid[y-1][x] == '@':
                    count += 1
                if x < m- 1 and y > 0 and grid[y-1][x+1] == '@':
                    count += 1
                if x > 0 and grid[y][x-1] == '@':
                    count += 1
                if x < m - 1 and grid[y][x+1] == '@':
                    count += 1
                if x > 0 and y < n - 1 and grid[y+1][x-1] == '@':
                    count += 1
                if y < n - 1 and grid[y+1][x] == '@':
                    count += 1
                if x < m - 1 and y < n - 1 and grid[y+1][x+1] == '@':
                    count += 1

                if count < 4:
                    removes.append((x,y))
                count = 0
    return removes

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
    assert ans1 == 1451
    assert ans2 == 8701
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
