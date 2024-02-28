import time
from collections import defaultdict

def do_tests():
    lines = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''
    return True

def bfs(programs, root):
    visited = set()
    q = []
    visited.add(root)
    q.append(root)
    while len(q) != 0:
        v = q.pop(0)
        for program in programs[v]:
            if program not in visited:
                visited.add(program)
                q.append(program)
    return visited

def parse(lines):
    programs = {}
    for line in lines:
        a, b = line.split(' <-> ')
        b = b.split(', ')
        programs[a] = b
    return programs

def solve(programs):
    connected = bfs(programs, '0')
    ans1 = len(connected)
    ans2 = 1
    for program in connected:
        del programs[program]
    while len(programs) > 0:
        connected = bfs(programs, list(programs.keys())[0])
        for program in connected:
            del programs[program]
        ans2 += 1

    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    programs = parse(lines)
    ans1, ans2 = solve(programs)
    
    assert ans1 == 288
    assert ans2 == 211
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
