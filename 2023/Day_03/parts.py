import sys
import time
import re

start = time.time()

numbers = []

lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]

for line in lines:
    numbers.append(re.findall(r'\d+', line))

print(f"All the numbers: {numbers}")

print(f"Total lines of input: {len(lines)}.")
end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")