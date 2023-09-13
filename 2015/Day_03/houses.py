f = open("input.txt", "r")
lines = f.readlines()

x = 0
y = 0
houses = {(x,y)}
moves = [x for x in lines[0]]
for move in moves:
    if move == '^':
        y += 1
    elif move == '>':
        x += 1
    elif move == 'v':
        y -= 1
    else: # '<'
        x -= 1
    houses.add((x,y))
print(f"Part 1: {len(houses)}, Part 2:")