import time
import re
    
def do_tests():
    return True

def main():
    start_time = time.time()

    lines = open(0).read().splitlines()
    guests = []
    for line in lines:
        guest = []
        line = line[:-1]
        line = line.split()
        sign = -1
        if line[2] == 'gain':
            sign = 1
        value = int(line[3]) * sign
        guest = [line[0], value, line[10]]
        guests.append(guest)
    for guest in guests:
        print(guest)

    if do_tests():
        print("Tests Passed")
    
    #assert ans1 == 111754
    #assert ans2 == 65402
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
