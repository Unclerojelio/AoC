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
            neighbors = 0
            if x == 0 and y == 0:
                neighbors = grid[0][1] + grid[1][1] + grid[1][0]
            elif x == len(grid[0])-1 and y == 0:
                neighbors = grid[y][x-1] + grid[y+1][x-1] + grid[y+1][x]
            elif x == len(grid[0])-1 and y == len(grid)-1:
                neighbors = grid[y-1][x] + grid[y-1][x-1] + grid[y][x-1]
            elif x == 0 and y == len(grid)-1:
                neighbors = grid[y-1][x] + grid[y-1][x+1] + grid[y][x+1]
            elif y == 0:
                neighbors = grid[y][x-1] + grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1] + grid[y][x+1]
            elif x == len(grid[0])-1:
                neighbors = grid[y-1][x] + grid[y-1][x-1] + grid[y][x-1] + grid[y+1][x-1] + grid[y+1][x]
            elif y == len(grid)-1:
                neighbors = grid[y][x+1] + grid[y-1][x+1] + grid[y-1][x] + grid[y-1][x-1] + grid[y][x-1]
            elif x == 0:
                neighbors = grid[y+1][x] + grid[y+1][x+1] + grid[y][x+1] + grid[y-1][x+1] + grid[y-1][x]
            else:
                neighbors = grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1] + grid[y][x+1] + grid[y+1][x+1] + grid[y+1][x] + grid[y+1][x-1] + grid[y][x-1]

            if grid[y][x] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
            if grid[y][x] == 0:
                if neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        next_grid.append(new_row)
    return next_grid

def solve(grid, steps, stuck):
    if stuck:
        grid[0][0] = 1
        grid[0][len(grid[0])-1] = 1
        grid[len(grid)-1][len(grid[0])-1] = 1
        grid[len(grid)-1][0] = 1

    # print(f'Initial State')
    # for row in grid:
    #     print(row)
    # print()

    for i in range(1, steps+1):
        grid = get_next(grid)
        if stuck:
            grid[0][0] = 1
            grid[0][len(grid[0])-1] = 1
            grid[len(grid)-1][len(grid[0])-1] = 1
            grid[len(grid)-1][0] = 1
        # print(f'After {i} steps')
        # for row in grid:
        #     print(row)
        # print()

    answer = sum([sum(row) for row in grid])
    return answer

def do_tests():
    lines = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''
    lines = lines.splitlines()
    grid = parse_file(lines)
    ans1 = solve(grid, 4, False)
    ans2 = solve(grid, 5, True)

    assert ans1 == 4
    assert ans2 == 17
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    grid = parse_file(open(0).read().splitlines())
    ans1 = solve(grid, 100, False)
    ans2 = solve(grid, 100, True)
    
    assert ans1 == 814
    assert ans2 == 924
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
