import sys

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
numbers = []
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in lines:
    # for word in words:
    #     results = [i for i in range(len(line)) if line.startswith(word, i)]
    #     for result in results:
    #         line = line[:result] + str(words.index(word)) + line[result+1:]
    # lineno += 1
    # print(lineno, firstandlast(line))
    # total += firstandlast(line)
    while len(line) > 0:
        if line[0].isdigit():
            numbers.append(line[0])
            line = line[1:]
        elif line.startswith("one")
print(total)