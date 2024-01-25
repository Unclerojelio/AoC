import time

start_time = time.time()
lines = open(0).read().splitlines()

xs = 10
ys = 10
lights = [[0]*xs]*ys

lines = ['turn on 0,0 through 0,0']

for line in lines:
    line = line.split(' ')
    if line[0] == 'turn':
        line = line[1:]
    cmd = line[0]
    start = line[1]
    end = line[3]
    start_x, start_y = start.split(',')
    end_x, end_y = end.split(',')
    start_x = int(start_x)
    start_y = int(start_y)
    end_x = int(end_x)
    end_y = int(end_y)
    # print(line)
    #print(cmd, start_x, start_y, end_x, end_y)

    if cmd == 'on':
        print(cmd, start_x, start_y, end_x, end_y)
        for y in range(start_y, end_y+1):
            for x in range(start_x, end_x+1):
                lights[y][x] = 1
        
    elif cmd == 'off':
        print(cmd, start_x, start_y, end_x, end_y)
        for y in range(start_y, end_y+1):
            for x in range(start_x, end_x+1):
                lights[y][x] = 0


    elif cmd == 'toggle':
        print(cmd, start_x, start_y, end_x, end_y)
        for y in range(start_y, end_y+1):
            for x in range(start_x, end_x+1):
                if lights[y][x] == 0:
                    lights[y][x] = 1
                else:
                    lights[y][x] = 0


count = 0
for y in range(ys):
    for x in range(xs):
        #print(lights[y])
        #count += sum(lights[y])
        print(lights[y][x], end=' ')
        count += lights[y][x]
    print()

#692000 is too high
print(f"Lights: {count}")

print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")