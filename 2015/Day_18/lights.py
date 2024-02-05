import time
import re
from itertools import combinations


def parse_file(lines):
  return lines

def solve(lines):
    ans1 = 0

    ans2 = 0

    return ans1, ans2

def do_tests():
    lines = '''1B5...
234...
......
..123.
..8A4.
..765.'''
    lines = lines.splitlines()
    lines = parse_file(lines)
    ans1, ans2 = solve(lines)

    # assert ans1 == 4
    # assert ans2 == 3
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    lines = parse_file(open(0).read().splitlines())
    ans1, ans2 = solve(lines)
    
    # assert ans1 == 654
    # assert ans2 == 405
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()