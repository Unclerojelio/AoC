import time
import re
from itertools import permutations

def do_tests():
    lines = '''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.'''

    lines = lines.splitlines()
    assert solve(lines) == 330
    return True

def solve(lines):
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

    return ans1

def main():
    start_time = time.time()

    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ans1 = solve(lines)
    
    assert ans1 == 709
    ans2 = 0
    #assert ans2 == 65402
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
