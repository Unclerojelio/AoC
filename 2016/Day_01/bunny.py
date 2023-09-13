def turn(heading, direction):
    if direction == 'R':
        if heading == "North":
            heading = "East"
        elif heading == "East":
            heading = "South"
        elif heading == "South":
            heading = "West"
        elif heading == "West":
            heading = "North"
    else: # turn left
        if heading == "North":
            heading = "West"
        elif heading == "East":
            heading = "North"
        elif heading == "South":
            heading = "East"
        elif heading == "West":
            heading = "South"
    return heading

def move(x, y, heading, distance, visited):
    if heading == "North":
        for _ in range(distance):
            y += 1
            visited.append((x,y))
    elif heading == "East":
        for _ in range(distance):
            x += 1
            visited.append((x,y))
    elif heading == "South":
        for _ in range(distance):
            y -= 1
            visited.append((x,y))
    elif heading == "West":
        for _ in range(distance):
            x -= 1
            visited.append((x,y))
    return x, y, visited

f = open("input.txt", "r")
line = f.readlines()
#line = ['R8, R4, R4, R8']
steps = line[0].split(',')
steps = [step.strip() for step in steps]

heading = 'North'
x = 0
y = 0
visited = [(0,0)]

for step in steps:
    heading = turn(heading, step[0])
    x, y, visited = move(x, y, heading, int(step[1:]), visited)

duplicates = [visit for visit in visited if visited.count(visit) > 1]
# for i in range(len(visited)):
#     if visited.count(visited[i]) > 1:
#         print(visited[i])

print(f"Part 1: {abs(x)+abs(y)} Part 2: {abs(duplicates[0][0]) + abs(duplicates[0][1])}")  