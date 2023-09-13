f = open("input.txt", "r")
lines = f.readlines()

def calculate_freq(sign, number):
    if sign == '+':
        return number
    else: #sign = '-'
        return number * -1

def sign(line):
    return line[0]

def number(line):
    return int(line[1:])

sum = 0
freqs = []
for line in lines:
    sum += calculate_freq(sign(line), number(line))
print(f"Part 1: {sum}")

freqs = []
freq = 0
while 1:
    for line in lines:
        freq += calculate_freq(sign(line), number(line))
        if freq not in freqs:
            freqs.append(freq)
        else:
            print(f"Part 2: {freq}")
            exit()
