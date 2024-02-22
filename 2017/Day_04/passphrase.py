import time
from itertools import permutations

def do_tests():
    lines = ''''''
    lines = lines.splitlines()
    ans1, ans2 = solve(lines)

    # assert ans1 == "easter"
    # assert ans2 == "advent"
    return True

def solve(lines):
    ans1 = 0
    ans2 = 0
    for line in lines:
        wordset = set()
        words = line.split()
        for word in words:
            wordset.add(word)
        if len(wordset) == len(words):
            ans1 += 1

        word = words[:1]
        words = words[1:]
        candidate = True
        while len(words) > 0 and candidate:
            for perm in list(permutations(word[0])):
                word = ''.join(perm)
                if word in words:
                    candidate = False
                    break
            word = words[:1]
            words = words[1:]
        if candidate:
            ans2 += 1

    return ans1, ans2

def main():
    start_time = time.time()
 
    # if do_tests():
    #     print("Tests Passed")

    lines = open(0).read().splitlines()
    ans1, ans2 = solve(lines)
    
    assert ans1 == 466
    assert ans2 == 251
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
