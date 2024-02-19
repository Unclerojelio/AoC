import time
import re
from collections import defaultdict

def do_tests():
    lines = ''''''
    lines = lines.splitlines()
    reindeer = parse_file(lines)
    ans1, ans2 = solve()

    #assert ans1 == 1120
    return True

def parse_file(lines):
    letter_counts = [defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)]
    for line in lines:
        for i, ch in enumerate(line):
            letter_counts[i][ch] += 1
    print(letter_counts)
    return letter_counts


def solve():
    ans1 = 0
    ans2 = 0
    return ans1, ans2

def main():
    start_time = time.time()

    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    letter_counts = parse_file(lines)
    for i in range(len(letter_counts)):
        print(max(zip(letter_counts[i].values(), letter_counts[i].keys()))[1])
    ans1, ans2 = solve()
    
    #assert ans1 == 2660
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
