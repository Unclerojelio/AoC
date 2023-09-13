f = open("2017/Day_01/input.txt", "r")
line = f.readlines()
line = line[0]

def captcha(line, step):
    sum = 0
    length = len(line)
    for i in range(length):
        if line[i] == line[(i + step) % length]:
            sum += int(line[i])
    return sum

print(f"Part 1: {captcha(line, 1)}")
print(f"Part 2: {captcha(line, len(line)//2)}")