import time

def do_tests():
    lines = '''0
    3
    0
    1
    -3'''
    lines = lines.splitlines()
    ans1 = solve1(lines)
    ans2 = solve2(lines)

    assert ans1 == 5
    assert ans2 == 10
    return True

def solve1(lines):
    ans1 = 0
    maze = []
    for line in lines:
        maze.append(int(line))

    i = 0
    done = False
    while not done:
        prev = i
        i = i + maze[i] 
        if i >= len(maze):
            done = True
        maze[prev] += 1
        ans1 += 1
        # for j, item in enumerate(maze):
        #     if j == i:
        #         item = '(' + str(item) + ')'
        #     print(item, end='\t')
        # print()
    return ans1

def solve2(lines):
    ans2 = 0
    maze = []
    for line in lines:
        maze.append(int(line))

    i = 0
    done = False
    while not done:
        prev = i
        i = i + maze[i] 
        if i >= len(maze):
            done = True
        if maze[prev] >= 3:
            maze[prev] -= 1
        else:
            maze[prev] += 1
        ans2 += 1
        # for j, item in enumerate(maze):
        #     if j == i:
        #         item = '(' + str(item) + ')'
        #     print(item, end='\t')
        # print()
    return ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ans1 = solve1(lines)
    ans2 = solve2(lines)
    
    assert ans1 == 343364
    assert ans2 == 25071947
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
