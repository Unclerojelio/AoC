# usage: python3 products.py < input.txt

import time
from collections import defaultdict

def do_tests():
    line = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
    ranges = parse(line)
    ans1, ans2 = solve(ranges)
    assert ans1 == 3
    assert ans2 == 6
    return True

def parse(line):
    ranges = line.split(",")
    return ranges

def solve(ranges):
    for range in ranges:
        start, end = range.split("-")
        if (len(start) % 2 == 0) and (len(end) % 2 == 0):
            print(start, end)
    return 0, 0

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    line = open(0).read()
    ranges = parse(line)
    ans1, ans2 = solve(ranges)
    assert ans1 == 1172
    assert ans2 == 6932
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
