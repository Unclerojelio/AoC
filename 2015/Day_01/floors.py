f = open("input.txt", "r")
line = f.readlines()
line = line[0]
floor = 0
floors = []
for i in range(len(line)):
    if line[i]  == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        floors.append(i)
print(f"Part 1: {floor} Part 2: {floors[0]+1}")