import time
import functools

def do_tests():
    line = 'flqrgnkx'
    ans1, ans2 = solve(line)
    #assert ans1 == 8108
    # assert ans2 == 10
    return True

def solve(line):
    ans1, ans2 = 0,0
    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).readlines()
    wire1 = lines[0].split(',')
    wire2 = lines[1].split(',')
    path1 = set()
    path2 = set()

    x = 0
    y = 0
    for location in wire1:
        dir = location[:1]
        dist = int(location[1:])
        if dir == 'U':
            y = y + dist
        elif dir == 'R':
            x = x + dist
        elif dir == "D":
            y = y - dist
        else:
            x = x - dist
        path1.add((x, y))

    x = 0
    y = 0
    for location in wire2:
        dir = location[:1]
        dist = int(location[1:])
        if dir == 'U':
            y = y + dist
        elif dir == 'R':
            x = x + dist
        elif dir == "D":
            y = y - dist
        else:
            x = x - dist
        path2.add((x, y))
    print(path1.intersection(path2))
    #print(wire2)
    #ans1, ans2 = solve(line)
    
    # assert ans1 == 1900
    # assert ans2 == 3966414
    #print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
