import time
from collections import defaultdict

def do_tests():
    lines = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
    ans1 = parse(lines.splitlines())
    #ans1, ans2 = solve(left_nums, right_nums)
    assert ans1 == 2
    assert ans2 == 31
    return True

def parse(lines):
    safe = 0
    for line in lines:
        if line[0] == line[1]:
            break
        elif line[0] > line[1]:
            increasing = True
        else:
            increasing = False

        for pos in range(0, len(line) - 2):
            valid = True
            if abs(int(line[pos]) - int(line[pos+1])) not in range(1,4):
                valid = False
                break
            if increasing and (line[pos] >= line[pos+1] or line[pos+1] - line[pos] not in range(1, 4)):
                valid = False
                break
            if not increasing and (line[pos] <= line[pos+1] or line[pos] - line[pos+1] not in range(1, 4)):
                valid = False
            if valid:
                safe = safe + 1
    return safe

def solve(left_nums, right_nums):
    distance = 0
    similarity = 0
    nums = list(zip(left_nums, right_nums))
    for pair in nums:
        distance = distance + abs(int(pair[0]) - int(pair[1]))
    for num in left_nums:
        similarity = similarity + int(num) * int(right_nums.count(num))
    print(similarity)
    return distance, similarity

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ans1 = parse(lines)
    #ans1, ans2 = solve(left_nums, right_nums)
    assert ans1 == 1830467
    assert ans2 == 26674158
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
