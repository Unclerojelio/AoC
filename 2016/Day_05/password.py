import time
import hashlib

class bcolors:
    HEADER =    '\033[95m'
    OKBLUE =    '\033[94m'
    OKCYAN =    '\033[96m'
    OKGREEN =   '\033[92m'
    WARNING =   '\033[93m'
    FAIL =      '\033[91m'
    ENDC =      '\033[0m'
    BOLD =      '\033[1m'
    UNDERLINE = '\033[4m'

lines = "cxdnnyjw"

def test():
    lines = "abc"
    if solve(lines) == "18f47a30":
        print(f"{bcolors.OKGREEN}Test passed{bcolors.ENDC}")
        return True
    else:
        print(f"{bcolors.FAIL}Test failed.{bcolors.ENDC}")
        return False

def solve(lines):
    ans1 = ""
    i = 0
    while len(ans1) < 8:
        h = hashlib.md5(f"{lines}{i}".encode()).hexdigest()
        if h.startswith("00000"):
            ans1 += h[5]
        i += 1
    return ans1

def main():
    start = time.time()

    if test():
        #lines = open(0).read().splitlines()
        ans1 = solve(lines)
        assert ans1 == "f77a0e6e"
        print(f"Answer 1: {ans1}")

    end = time.time()
    print("Elapsed time:", (end-start) * 10**3, "ms")


if __name__=="__main__":
    main()
