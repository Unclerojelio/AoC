import time

def do_tests():
    line = '''{}'''
    ans1, ans2 = solve(line)
    assert ans1 == 1
    line = '''{{{}}}'''
    ans1, ans2 = solve(line)
    assert ans1 == 6
    line = '''{{},{}}'''
    ans1, ans2 = solve(line)
    assert ans1 == 5
    line = '''{{{},{},{{}}}}'''
    ans1, ans2 = solve(line)
    assert ans1 == 16
    line = '''{<a>,<a>,<a>,<a>}'''
    ans1, ans2 = solve(line)
    assert ans1 == 1
    line = '''{{<ab>},{<ab>},{<ab>},{<ab>}}'''
    ans1, ans2 = solve(line)
    assert ans1 == 9
    line = '''{{<!!>},{<!!>},{<!!>},{<!!>}}'''
    ans1, ans2 = solve(line)
    assert ans1 == 9
    line = '''{{<a!>},{<a!>},{<a!>},{<ab>}}'''
    ans1, ans2 = solve(line)
    assert ans1 == 3
    # assert ans2 == 4
    return True

def solve(line):
    ans1 = 0
    ans2 = 0
    stack = []
    score = 0
    for ch in line:
        if ch == '{':
            score += 1
            stack.append(ch)
        elif ch == '}':
            ans1 += score
            score -= 1
    print(ans1)
    return ans1, ans2


def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    line = open(0).read()
    ans1, ans2 = solve(line)
    
    # assert ans1 == 12841
    # assert ans2 == 8038
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
