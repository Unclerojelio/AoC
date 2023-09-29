f = open("input.txt", "r")
lines = f.readlines()

map = []
for line in lines:
    map.append(line.rstrip())

def count_trees(map, slopes):
    product = 1
    for slope in slopes:
        x = 0
        y = 0
        count = 0
        for i in range(slope[1], len(map), slope[1]):
            x += slope[0]
            x = x % len(line)
            if map[i][x] == '#':
                count += 1
        product *= count
    return product

print(f"Part 1: {count_trees(map, [(3,1)])} Part 2: {count_trees(map, [(1,1), (3,1), (5,1), (7,1), (1,2)])}")