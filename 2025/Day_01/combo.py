# usage: python3 combo.py < input.txt

import time
from collections import defaultdict

def do_tests():
    lines = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''
    moves = lines.splitlines()
    ans1, ans2 = solve(moves)
    assert ans1 == 3
    assert ans2 == 6
    return True

# def parse(lines):
#     left_nums = []
#     right_nums = []
#     for line in lines:
#         left_num, right_num = line.split()
#         left_nums.append(left_num)
#         right_nums.append(right_num)
#     left_nums.sort()
#     right_nums.sort()
#     return left_nums, right_nums

def solve(moves):
    current = 50
    combo = 0
    passes = 0
    for move in moves:
        print(current, passes)
        direction = move[0]
        distance = int(move[1:])
        passes = passes + distance // 100
        if direction == 'L':
            if (current - distance < 0) and (current != 0):
                passes += 1
            current = (current - distance) % 100

        else:
            if (current + distance > 100):
                passes += 1
            current = (current + distance) % 100

        if current == 0:
            combo += 1
    print(current, passes)
    print(combo, combo + passes)
    return combo, combo + passes

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    moves = open(0).read().splitlines()
    # left_nums, right_nums = parse(lines)
    ans1, ans2 = solve(moves)
    assert ans1 == 1172
    #assert ans2 == 7507 too high
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
