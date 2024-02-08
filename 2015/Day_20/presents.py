import time
import re
import itertools
import math

def divisors(n) :
    result = []
    if(n == 1):
        result.append(1)
        return result

    for i in range(2,(int)(math.sqrt(n))+1) :
        if (n % i == 0) :
            if (i == (n/i)) :
                result.append(i)
            else :
                result.extend([i, n//i])
    result.extend([1, n])
    return result

def sumdiv(n) :
    result = 0
    for i in range(2,(int)(math.sqrt(n))) :
        if (n % i == 0) :
            if (i == (n/i)) :
                if 50 * i >= n:
                    result = result + i
            else :
                if 50 * i >= n:
                    result = result + i
                if 50 * (n/i) >= n:
                    result = result + (n / i)
    return int(result + n)

def solve(goal):
    for i in itertools.count():
        presents = 10 * sum(divisors(i))
        if presents >= goal:
            return i

def solve2(goal):
    for i in itertools.count():
        presents = 11 * sumdiv(i)
        if presents >= goal:
            return i

def main():
    start_time = time.time()
    ans1 = 0
    #ans1 = solve(29000000)
    ans2 = solve2(29000000)
    
    #assert ans1 == 665280
    assert ans2 == 705600
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
