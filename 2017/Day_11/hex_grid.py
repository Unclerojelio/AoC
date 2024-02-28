# Axial coordinates and distance from: https://www.redblobgames.com/grids/hexagons/

import time

def do_tests():
    line = '''{}'''
    return True

def solve(steps):
    def dist(q,r):
        return (abs(q) + abs(q + r) + abs(r)) // 2
    
    furthest = 0
    directions = {'n': (0, -1), 'ne': (1, -1), 'se': (1, 0), 's': (0, 1), 'sw': (-1, 1), 'nw': (-1,0)}
    ans1 = 0
    ans2 = 0
    q, r = 0,0
    for step in steps:
        dq, dr = directions[step]
        q += dq
        r += dr
        furthest = max(furthest, dist(q,r))
    
    return dist(q,r), furthest


def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    steps = open(0).read().strip().split(',')

    ans1, ans2 = solve(steps)
    
    assert ans1 == 794
    assert ans2 == 1524
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
