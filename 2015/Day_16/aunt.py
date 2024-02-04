import time
import re
from itertools import permutations


def parse_file(lines):
    aunts = []
    for line in lines:
        aunt = line.split()
        aunts.append({'Number': aunt[1][:-1], aunt[2][:-1]: aunt[3][:-1], aunt[4][:-1]: aunt[5][:-1], aunt[6][:-1]: aunt[7]})
    return aunts

def solve(aunts):
    aunt_sue = {'children': '3', 
                'cats': '7',
                'samoyeds': '2', 
                'pomeranians': '3', 
                'akitas': '0', 
                'vizslas': '0', 
                'goldfish': '5', 
                'trees': '3', 
                'cars': '2', 
                'perfumes': '1'}
    for aunt in aunts:
        count = 0
        for key in aunt_sue.keys():
            if key in aunt.keys() and aunt_sue[key] == aunt[key]:
                count += 1
            if count == 3:
                ans1 = int(aunt['Number'])
    ans2 = 0
    return ans1, ans2

def main():
    start_time = time.time()
    aunts = parse_file(open(0).read().splitlines())
    ans1, ans2 = solve(aunts)
    
    assert ans1 == 103
    # assert ans2 == 15862900
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()