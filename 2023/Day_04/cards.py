import sys
import time

start = time.time()

#lines = sys.stdin.readlines()
#lines = [line.rstrip() for line in lines]

lines = open(0).read().splitlines()
sum = 0
for line in lines:
    index = line.find(":")
    line = line[index+1:]
    winners, choices = line.split("|")
    winners = winners.split()
    choices = choices.split()
    count = 0
    for choice in choices:
        if choice in winners:
            count += 1
    if count >= 1:
        sum += 2**(count - 1)
assert sum == 24160
print(f"The answer for part 1: {sum}")

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")