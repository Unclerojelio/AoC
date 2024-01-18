import sys
import time

start = time.time()

#lines = sys.stdin.readlines()
#lines = [line.rstrip() for line in lines]

lines = open(0).read().splitlines()

print(lines)

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")