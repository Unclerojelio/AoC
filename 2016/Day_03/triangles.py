import time

start = time.time()

lines = open(0).read().splitlines()

possibles = 0

for line in lines:
    a, b, c  = map(int, line.split())
    if (a + b > c) and (a + c > b) and (b + c > a):
        possibles += 1

assert possibles == 982
print(f"Answer 1: {possibles}")


possibles2 = 0
while len(lines) != 0:
    three_lines = lines[:3]
    lines = lines[3:]
    a1, a2, a3 = map(int, three_lines[0].split())
    b1, b2, b3 = map(int, three_lines[1].split())
    c1, c2, c3 = map(int, three_lines[2].split())
    if (a1 + b1 > c1) and (a1 + c1 > b1) and (b1 + c1 > a1):
        possibles2 += 1
    if (a2 + b2 > c2) and (a2 + c2 > b2) and (b2 + c2 > a2):
        possibles2 += 1
    if (a3 + b3 > c3) and (a3 + c3 > b3) and (b3 + c3 > a3):
        possibles2 += 1

assert possibles2 == 1826
print(f"Answer 2: {possibles2}")

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")