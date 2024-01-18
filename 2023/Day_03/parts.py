#Thanks to HyperNeutrino on YouTube.

import sys
import time

start = time.time()

cs = set()
lines = sys.stdin.readlines()
grid = [line.rstrip() for line in lines]

for r, row in enumerate(grid):
    for c , ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc - 1]. isdigit():
                    cc -= 1
                cs.add((cr, cc))
                
ns = []
for r, c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c  += 1
    ns.append(int(s))
ans1 = sum(ns)
assert ans1 == 507214

ans2 = 0
for r, row in enumerate(grid):
    for c , ch in enumerate(row):
        if ch != '*':
            continue

        cs = set()

        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc - 1]. isdigit():
                    cc -= 1
                cs.add((cr, cc))

        if len(cs) != 2:
            continue
        ns = []
        for cr, cc in cs:
            s = ""
            while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                s += grid[cr][cc]
                cc  += 1
            ns.append(int(s))
        ans2 += ns[0] * ns[1]
assert ans2 == 72553319

print(f"The answer to Part 1 is: {ans1} The answer to Part 2 is: {ans2}.")

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")