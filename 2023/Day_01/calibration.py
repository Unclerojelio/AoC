import sys
import time

start = time.time()

def firstandlast(line):
    digits = []
    for c in line:
        if c.isdigit():
            digits += c
    #print(int(digits[0] + digits[-1]))
    return int(digits[0] + digits[-1])

lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]

total = 0
for line in lines:
    total += firstandlast(line)
assert total == 55017
print(total)

total = 0
lineno = 0
for line in lines:
    lineno += 1
    numbers = []
    while len(line) > 0:
        if line[0].isdigit():
            numbers.append(line[0])
            line = line[1:]
        elif line.startswith("one"):
            numbers.append("1")
            line = line[1:]
        elif line.startswith("two"):
            numbers.append("2")
            line = line[1:]
        elif line.startswith("three"):
            numbers.append("3")
            line = line[1:]
        elif line.startswith("four"):
            numbers.append("4")
            line = line[1:]
        elif line.startswith("five"):
            numbers.append("5")
            line = line[1:]
        elif line.startswith("six"):
            numbers.append("6")
            line = line[1:]
        elif line.startswith("seven"):
            numbers.append("7")
            line = line[1:]
        elif line.startswith("eight"):
            numbers.append("8")
            line = line[1:]
        elif line.startswith("nine"):
            numbers.append("9")
            line = line[1:]
        else:
            line = line[1:]
    total += firstandlast(numbers)
assert total == 53539
print(total)

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")
