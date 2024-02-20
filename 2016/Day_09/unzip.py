import time

def do_tests():
    ans1, ans2 = solve('ADVENT')
    assert ans1 == 6
    ans1, ans2 = solve('A(1x5)BC')
    assert ans1 == 7
    ans1, asn2 = solve('(3x3)XYZ')
    assert ans1 == 9
    ans1, ans2 = solve('(6x1)(1x3)A')
    assert ans1 == 6
    ans1, ans2 = solve('X(8x2)(3x3)ABCY')
    assert ans1 == 18
    return True

def solve(file):
    ans1 = 0
    ans2 = 0
    i = 0
    ans1 = 0
    f_iter = iter(file)
    c = next(f_iter)
    while c:
        if c != '(':
            ans1 += 1
            c = next(f_iter, False)
            continue
        group = ''
        c = next(f_iter)
        while c != ')':
            group += c
            c = next(f_iter)
        c = next(f_iter) #discard closing paren
        x, y = group.split('x')
        for i in range(int(x)):
            c = next(f_iter, False)
        ans1 += int(x) * int(y)
    return ans1, ans2

def main():
    start_time = time.time()

    if do_tests():
        print("Tests Passed")
    else:
        print("Test Failed")

    file = open(0).read()
    ans1, ans2 = solve(file)
    
    assert ans1 == 112830
    #original text length = 17279
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
