import time
from collections import defaultdict

def do_tests():
    lines = '''0: 3
1: 2
4: 4
6: 4'''
    firewall = parse(lines.splitlines())
    ans1, ans2 = solve(firewall)
    assert ans1 == 24
    assert ans2 == 10
    return True

def final_index(length, n):
    # The first draft from ChatGPT of this function was incorrect. I tweaked it to work.
    if length == 1:
        return 0
    remainder = n % (2 * (length - 1))
    if remainder == 0:
        return 0
    if remainder <= length - 1:
        return remainder
    return length - remainder - 1

def parse(lines):
    firewall = {}
    for line in lines:
        layer, rng = line.split(': ')
        firewall[int(layer)] = int(rng)
    return firewall

def solve(firewall):
    ans1, ans2 = 0,0
    for layer in firewall:
        if final_index(firewall[layer], layer) == 0:
            ans1 += firewall[layer] * layer

    free_path = False
    while not free_path:
        free_path = True
        for layer in firewall:
            if final_index(firewall[layer], layer + ans2) == 0:
                free_path = False
                break
        ans2 += 1

    return ans1, ans2 - 1

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    firewall = parse(lines)
    ans1, ans2 = solve(firewall)
    
    assert ans1 == 1900
    assert ans2 == 3966414
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
