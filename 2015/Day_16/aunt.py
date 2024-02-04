import time
import re
from itertools import permutations


def parse_file(lines):
    aunts = []
    for line in lines:
        aunt = line.split()
        aunts.append({'Number': aunt[1][:-1], aunt[2][:-1]: aunt[3][:-1], aunt[4][:-1]: aunt[5][:-1], aunt[6][:-1]: aunt[7]})
    return aunts

def solve(lines):
    ans1 = 0
    ans2 = 0
    return ans1, ans2

def main():
    start_time = time.time()
    aunts = parse_file(open(0).read().splitlines())
    ans1, ans2 = solve(aunts)
    
    # assert ans1 == 18965440
    # assert ans2 == 15862900
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()