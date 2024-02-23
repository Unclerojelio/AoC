import time

def do_tests():
    line = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''
    lines = lines.splitlines()
  for line in lines:
    print(line)
    
    ans1, ans2 = solve()

    # assert ans1 == 5
    # assert ans2 == 4
    return True

def solve(blocks):
  ans1 = 0
  ans2 = 0
  return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    ans1, ans2 = solve()
    
    # assert ans1 == 12841
    # assert ans2 == 8038
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
