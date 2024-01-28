# This doesn't wotk with Python3

import time

def solve():
    with open('input.txt', 'r') as f:
        str_len = 0
        mem_len = 0
        for line in f.readlines():
            str_len += len(line.strip())
            mem_len += len(eval(line))
        return str_len - mem_len

def main():
    start = time.time()

    ans1 = solve()
    assert ans1 == 1333
    print("Answer 1:", ans1)

    end = time.time()
    print("Elapsed time:", (end-start) * 10**3, "ms")


if __name__=="__main__":
    main()