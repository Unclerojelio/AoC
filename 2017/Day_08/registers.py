import time
from collections import defaultdict

def do_tests():
    lines = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''
    lines = lines.splitlines()
    ans1, ans2 = solve(lines)

    assert ans1 == 1
    assert ans2 == 10
    return True

def solve(lines):
    ans2 = 0
    registers = defaultdict(int)
    for line in lines:
        tokens = line.split()
        expr = str(registers[tokens[4]]) + tokens[5] + tokens[6]
        if eval(expr):
            if tokens[1] == 'inc':
                registers[tokens[0]] += int(tokens[2])
            else:
                registers[tokens[0]] -= int(tokens[2])
            ans2 = max(ans2, registers[tokens[0]])

    ans1 = max(registers.values())

    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ans1, ans2 = solve(lines)
    
    assert ans1 == 8022
    assert ans2 == 9819
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
