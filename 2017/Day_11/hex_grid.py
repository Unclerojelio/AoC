import time

def do_tests():
    line = '''{}'''
    return True

def solve(steps):
    ans1 = 0
    ans2 = 0
    return ans1, ans2


def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    steps = open(0).read().strip().split(',')

    ans1, ans2 = solve(steps)
    
    # assert ans1 == 16869
    # assert ans2 == 7284
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
