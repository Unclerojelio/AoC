import time
import re
from itertools import combinations

def solve():
    answer = 0
    return answer

def do_tests():
    ans1 = solve()
    ans2 = solve()

    # assert ans1 == 4
    # assert ans2 == 17
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    ans1 = solve()
    ans2 = solve()
    
    # assert ans1 == 814
    # assert ans2 == 924
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
