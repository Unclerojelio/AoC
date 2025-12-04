# usage: python3 joltage.py < input.txt

import time
from collections import defaultdict

def do_tests():
    lines = '''987654321111111
811111111111119
234234234234278
818181911112111'''
    banks = parse(lines)
    ans1, ans2 = solve(banks)
    assert ans1 == 357
    assert ans2 == 3121910778619
    return True

def parse(lines):
    banks = lines.splitlines()
    return banks

def solve(banks):
    ans1 = 0
    ans2 = 0
    for bank in banks:
        highest = 0
        for i in range(0, len(bank)-1):
            for j in range(i+1, len(bank)):
                num = int(bank[i] + bank[j])
                if num > highest:
                    highest = num
        ans1 += highest
        bank = list(map(int, bank.strip()))
        jolts = 0
        for index in range(11):
            digit = max(bank[:index - 11])
            bank = bank[bank.index(digit) + 1:]
            jolts = (jolts * 10) + digit
        jolts = (jolts * 10) + max(bank)
        ans2 += jolts
    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read()
    banks = parse(lines)
    ans1, ans2 = solve(banks)
    print(ans2)
    assert ans1 == 16793817782
    assert ans2 == 6932
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
