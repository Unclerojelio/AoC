import time
import re
from itertools import combinations


def parse_file(lines):
    grid = []
    for line in lines:
        row = []
        for ch in line:
            if ch == '.':
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid

def get_next(grid):
    next_grid = []
    for y in range(len(grid)):
        new_row = []
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                new_row.append(0)
            else:
                new_row.append(1)
        next_grid.append(new_row)
    return next_grid

def solve(grid, steps):
    for _ in range(steps):
        grid = get_next(grid)

    ans1 = sum([sum(row) for row in grid])
    ans2 = 0

    return ans1, ans2

def do_tests():
    lines = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''
    lines = lines.splitlines()
    grid = parse_file(lines)
    ans1, ans2 = solve(grid, 5)

    assert ans1 == 21
    # assert ans2 == 3
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    grid = parse_file(open(0).read().splitlines())
    ans1, ans2 = solve(grid, 101)
    
    # assert ans1 == 654
    # assert ans2 == 405
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
