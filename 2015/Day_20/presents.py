import time
import re
import itertools
import math

def divSum(n) :
    if(n == 1):
       return 1

    result = 0
    for i in range(2,(int)(math.sqrt(n))+1) :
        if (n % i == 0) :
            if (i == (n/i)) :
                result = result + i
            else :
                result = result + (i + n//i)

    return (result + n + 1)

def solve(goal):
    for i in itertools.count():
        presents = 10*divSum(i)
        if presents >= goal:
            return i


def main():
    start_time = time.time()

    ans1 = solve(29000000)
    ans2 = 0
    
    assert ans1 == 665280
    # assert ans2 == 924
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
