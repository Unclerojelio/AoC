f = open("2018/Day_03/input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

largestX = 0
largestY = 0
for line in lines:
    id, remains = line.strip().split('@')
    position, dimensions = remains.strip().split(':')
    x, y = position.strip().split(',')
    l, w = dimensions.strip().split('x')
    #print(id, x, y, l, w)
    if int(x) + int(w) > largestX:
        largestX = int(x) + int(w)
    if int(y) + int(l) > largestY:
        largestY = int(y) + int(l)
    #print(largestX, largestY)

fabric = []
for i in range(largestX):
    for j in range(largestY):
        fabric[i][j] = 0

