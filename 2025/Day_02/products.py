# usage: python3 products.py < input.txt

import time
from collections import defaultdict

def do_tests():
    line = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
    numbers = parse(line)
    ans1, ans2 = solve(numbers)
    assert ans1 == 1227775554
    assert ans2 == 4174379265
    return True

def parse(line):
    numbers = []
    ranges = line.split(",")
    for item in ranges:
        start, end = item.split("-")
        for number in range(int(start), int(end)+1):
            numbers.append(number)
    #print(numbers)
    return numbers

def solve(numbers):
    ans1 = 0
    ans2 = 0
    for number in numbers:
        s = str(number)
        if len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]:
            ans1 += number
        for i in range(2, len(s)+1):
            if len(s) % i == 0 and s[:len(s) // i] * i == s:
                ans2 += number
                break
    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    line = open(0).read()
    numbers = parse(line)
    ans1, ans2 = solve(numbers)
    print(ans2)
    assert ans1 == 16793817782
    assert ans2 == 6932
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
