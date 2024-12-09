import time
from collections import defaultdict

data = []

def do_tests():
    lines = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
    ans1 = parse(lines.splitlines())
    ans1, ans2 = solve(data)
    assert ans1 == 2
    assert ans2 == 31
    return True

def parse(lines):
    for line in lines:
        items = line.split()
        data.append(items)
    return data

def solve(data):
    safe = 0
    similarity = 0
    for report in data:
        level_set = set()
        for level in report:
            level_set.add(level)
        if len(report) == len(level_set) and (report == sorted(report) or report == sorted(report, reverse=True)):
            safe = safe + 1
    print(safe)
    return safe, similarity

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ans1 = parse(lines)
    ans1, ans2 = solve(data)
    assert ans1 == 1830467
    assert ans2 == 26674158
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
