import time
import re
from itertools import combinations

def solve():

    house = 1
    presents = 0
    elf = 1
    while presents <= 29000000:
        presents += elf * 10
        house += 1
        elf += 1

    print(house, elf, presents)
    return house

def main():
    start_time = time.time()
    

    ans1 = solve()
    ans2 = 0
    
    # assert ans1 == 814
    # assert ans2 == 924
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
