f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

paper = 0
ribbon = 0
for line in lines:
    l, w, h = line.split('x')
    dimensions = [int(l), int(w), int(h)]
    dimensions.sort()
    area =  2 * dimensions[0] * dimensions[1] + 2 * dimensions[1] * dimensions[2] + 2 * dimensions[0] * dimensions[2]
    smallest_side = dimensions[0] * dimensions[1]
    smallest_perimeter = 2 * dimensions[0] + 2 * dimensions[1]
    bow = dimensions[0] * dimensions[1] * dimensions[2]
    paper += area + smallest_side
    ribbon += smallest_perimeter + bow

print(f"Part 1: {paper} Part 2: {ribbon}")
