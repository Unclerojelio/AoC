import time
import re
from collections import defaultdict

def do_tests():
    lines = ''''''
    lines = lines.splitlines()
    letter_counts = parse_file(lines)
    ans1, ans2 = solve()

    # assert ans1 == "easter"
    # assert ans2 == "advent"
    return True

def parse_file(lines):
    addresses = lines
    return addresses


def solve(addresses):
    ans1 = ""
    ans2 = ""
    for address in addresses:
        print(address)
    return ans1, ans2

def main():
    start_time = time.time()

    # length of test data is different than input data. 
    # if do_tests():
    #     print("Tests Passed")

    lines = open(0).read().splitlines()
    addresses = parse_file(lines)
    ans1, ans2 = solve(addresses)
    
    # assert ans1 == "umejzgdw"
    # assert ans2 == "aovueakv"
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()