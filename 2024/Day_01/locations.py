import time
from collections import defaultdict

def do_tests():
    lines = '''3   4
4   3
2   5
1   3
3   9
3   3'''
    left_nums, right_nums = parse(lines.splitlines())
    ans1, ans2 = solve(left_nums, right_nums)
    assert ans1 == 11
    assert ans2 == 31
    return True

def parse(lines):
    left_nums = []
    right_nums = []
    for line in lines:
        left_num, right_num = line.split()
        left_nums.append(left_num)
        right_nums.append(right_num)
    left_nums.sort()
    right_nums.sort()
    return left_nums, right_nums

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
    left_nums, right_nums = parse(lines)
    ans1, ans2 = solve(left_nums, right_nums)
    assert ans1 == 1830467
    assert ans2 == 26674158
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
