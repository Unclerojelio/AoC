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
    assert ans2 == 0
    return True

def parse(lines):
    grid = [list(line) for line in lines.strip().splitlines()]
    #print(grid)
    return grid

def solve(grid):
    ans1 = 0
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            #print(x,y, grid[y][x])
            if grid[y][x] == '@':
                if x > 0 and y > 0 and grid[y-1][x-1] == '@':
                    count += 1
                if y > 0 and grid[y-1][x] == '@':
                    count += 1
                if x < len(grid[0])- 1 and y > 0 and grid[y-1][x+1] == '@':
                    count += 1
                if x > 0 and grid[y][x-1] == '@':
                    count += 1
                if x < len(grid[0]) - 1 and grid[y][x+1] == '@':
                    count += 1
                if x > 0 and y < len(grid) - 1 and grid[y+1][x-1] == '@':
                    count += 1
                if y < len(grid) - 1 and grid[y+1][x] == '@':
                    count += 1
                if x < len(grid[0]) - 1 and y < len(grid) - 1 and grid[y+1][x+1] == '@':
                    count += 1

                if count < 4:
                    ans1 += 1
                count = 0
    #print(ans1)
    ans2 = 0
    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read()
    banks = parse(lines)
    ans1, ans2 = solve(banks)
    assert ans1 == 1451
    assert ans2 == 0
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
