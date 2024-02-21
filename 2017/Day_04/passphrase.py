import time

def do_tests():
    lines = ''''''
    lines = lines.splitlines()
    ans1, ans2 = solve(lines)

    # assert ans1 == "easter"
    # assert ans2 == "advent"
    return True

def solve(lines):
    ans1 = len(lines)
    ans2 = 0
    return ans1, ans2

def main():
    start_time = time.time()
 
    # if do_tests():
    #     print("Tests Passed")

    ans1 = 0
    ans2 = 0

    lines = open(0).read().splitlines()
    ans1, ans2 = solve(lines)
    
    # assert ans1 == 121
    # assert ans2 == "aovueakv"
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
