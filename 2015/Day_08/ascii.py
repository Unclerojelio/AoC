# This doesn't work with Python3
# because eval() has changed.

import time

def solve():
    with open('input.txt', 'r') as f:
        str_len = 0
        mem_len = 0
        num_chars = 0
        for line in f.readlines():
            str_len += len(line.strip())
            mem_len += len(eval(line))
            quote_count = line.strip().count('"')
            backslash_count = line.strip().count('\\')
            num_chars += len(line.strip()) + quote_count + backslash_count + 2
        ans1 = str_len - mem_len
        ans2 = num_chars - str_len
        return [ans1, ans2]

def main():
    start = time.time()

    ans1, ans2 = solve()
    assert ans1 == 1333
    assert ans2 == 2046
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    end = time.time()
    print("Elapsed time:", (end-start) * 10**3, "ms")


if __name__=="__main__":
    main()