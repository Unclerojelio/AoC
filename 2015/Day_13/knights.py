import time
import re
from itertools import permutations

def do_tests():
    return True

def main():
    start_time = time.time()

    lines = open(0).read().splitlines()
    pairs = {}
    guests = set()
    for line in lines:
        guest = []
        line = line[:-1]
        line = line.split()
        sign = -1
        if line[2] == 'gain':
            sign = 1
        guests.add(line[0])
        pairs[(line[0], line[10])] = int(line[3]) * sign

    ans1 = 0
    positions = permutations(guests)
    for position in positions:
        happiness = 0
        for i in range(len(position)):
            happiness += pairs[position[i], position[(i+1) % len(position)]]
            happiness += pairs[position[i], position[(i-1) % len(position)]]
        ans1 = max(ans1, happiness)
    print(ans1)


    if do_tests():
        print("Tests Passed")
    
    #assert ans1 == 111754
    #assert ans2 == 65402
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
