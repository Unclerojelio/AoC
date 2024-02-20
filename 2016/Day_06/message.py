import time
import re
from collections import defaultdict

def do_tests():
    lines = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''
    lines = lines.splitlines()
    letter_counts = parse_file(lines)
    print(letter_counts)
    ans1, ans2 = solve(letter_counts)

    assert ans1 == "easter"
    assert ans2 == "advent"
    return True

def parse_file(lines):
    letter_counts = [defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)]
    for line in lines:
        for i, ch in enumerate(line):
            letter_counts[i][ch] += 1
    return letter_counts


def solve(letter_counts):
    ans1 = ""
    ans2 = ""
    for i in range(len(letter_counts)):
        ans1 += max(zip(letter_counts[i].values(), letter_counts[i].keys()))[1]
        ans2 += min(zip(letter_counts[i].values(), letter_counts[i].keys()))[1]
    return ans1, ans2

def main():
    start_time = time.time()

    # length of test data is different than input data. 
    # if do_tests():
    #     print("Tests Passed")

    lines = open(0).read().splitlines()
    letter_counts = parse_file(lines)
    ans1, ans2 = solve(letter_counts)
    
    assert ans1 == "umejzgdw"
    assert ans2 == "aovueakv"
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
