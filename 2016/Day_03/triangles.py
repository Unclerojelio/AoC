import time

start = time.time()

lines = open(0).read().splitlines()

possibles = 0

for line in lines:
    a, b, c  = map(int, line.split())
    #print(f"Side: {a} {b} {c}")
    if (a + b > c) and (a + c > b) and (b + c > a):
        possibles += 1

assert possibles == 982
print(f"Answer 1: {possibles}")

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")