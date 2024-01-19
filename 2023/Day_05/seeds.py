import time

start = time.time()

seeds, *blocks = open(0).read().split("\n\n")

seeds = list(map(int,seeds.split(':')[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        a, b, c  = map(int, line.split())
        ranges.append((a, b, c))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c:
                new.append(x - b + a)
                break
        else:
            new.append(x)

    seeds = new
print(min(seeds))


end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")