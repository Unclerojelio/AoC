import time

start_time = time.time()
lines = open(0).read().splitlines()
for line in lines:
    print(line)



print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")