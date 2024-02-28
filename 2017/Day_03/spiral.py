import time
from collections import defaultdict

grid = defaultdict(int)

def get_spiral():
    def populate_grid(x, y):
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not (dx, dy) == (0,0):
                    total += grid[(x + dx, y + dy)]
        grid[(x, y)] = total

    grid[(0,0)] = 1
    yield grid[(0,0)]
    x, y = 1,0
    grid[(x,y)] = 1
    yield grid[(x,y)]
    while True:
        # go up
        while grid[(x-1, y)]:
            y += 1
            populate_grid(x,y)
            yield grid[(x,y)]
        # go left
        while grid[(x, y-1)]:
            x -= 1
            populate_grid(x,y)
            yield grid[(x,y)]
        # go down
        while grid[(x+1, y)]:
            y -= 1
            populate_grid(x,y)
            yield grid[(x,y)]
         # go right
        while grid[(x, y+1)]:
            x += 1
            populate_grid(x,y)
            yield grid[(x,y)]

def solve(input):
    ans1 = 0
    for ans1 in get_spiral():
        if ans1 > input:
            return ans1

def main():
    start_time = time.time()
    input = 368078
    ans1 = solve(input)
 
    print("Answer 1:", ans1)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()