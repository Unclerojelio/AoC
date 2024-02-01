import time
import re
from itertools import permutations

def do_tests():
    # assert ans1 == 330
    # assert ans2 == 286
    return True

def parse_file():
    reindeers = {}
    lines = open(0).read().splitlines()
    for line in lines:
        line = line.split()
        reindeers[line[0]] = (line[3], line[6], line[13])
    return reindeers


def solve(reindeers):
    for reindeer in reindeers:
        print(reindeer, reindeers[reindeer])
    ans1 = 0
    return ans1

def main():
    start_time = time.time()

    ans1 = 0
    ans2 = 0

    if do_tests():
        print("Tests Passed")


    #lines = open(0).read().splitlines()
    reindeer = parse_file()
    ans1 = solve(reindeer)
    
    # assert ans1 == 709
    # assert ans2 == 668
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()