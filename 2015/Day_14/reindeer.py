import time
import re
from itertools import permutations

def do_tests(race_time):
    lines = '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''
    lines = lines.splitlines()
    reindeer = parse_file(lines)
    ans1, ans2 = solve(reindeer, race_time)

    assert ans1 == 1120
    return True

def parse_file(lines):
    reindeers = {}
    for line in lines:
        line = line.split()
        # [0:"speed", 1:"stamina", 2:"rest_time", 3:"distance_traveled, 4:"points", 5:"racing_count", 6:"resting_count", 7:"resting"]
        reindeers[line[0]] = [line[3], line[6], line[13], 0, 0, 0, 0, False]
    return reindeers


def solve(reindeers, race_time):
    ans1 = 0
    for reindeer in reindeers:
        speed = int(reindeers[reindeer][0])
        stamina = int(reindeers[reindeer][1])
        rest = int(reindeers[reindeer][2])
        period = stamina + rest
        cycles = race_time // period
        distance = cycles * speed * stamina
        distance += speed * min((race_time % period), stamina)
        ans1 = max(ans1, distance)

    for second in range(race_time):
        distances = []
        for reindeer in reindeers:
            if not reindeers[reindeer][7]:  #resting
                reindeers[reindeer][3] += int(reindeers[reindeer][0])
                reindeers[reindeer][5] += 1
                if int(reindeers[reindeer][1]) == reindeers[reindeer][5]:
                    reindeers[reindeer][7] = True
                    reindeers[reindeer][5] = 0
            else:
                reindeers[reindeer][6] += 1
                if int(reindeers[reindeer][2]) == reindeers[reindeer][6]:
                    reindeers[reindeer][7] = False
                    reindeers[reindeer][6] = 0
            distances.append(reindeers[reindeer][3])
        farthest = max(distances)
        for reindeer in reindeers:
            if reindeers[reindeer][3] == farthest:
                reindeers[reindeer][4] += 1
    ans2 = 0
    for reindeer in reindeers:
        ans2 = max(ans2, reindeers[reindeer][4])

    return ans1, ans2

def main():
    start_time = time.time()

    if do_tests(1000):
        print("Tests Passed")

    lines = open(0).read().splitlines()
    race_time = 2503
    reindeer = parse_file(lines)
    ans1, ans2 = solve(reindeer, race_time)
    
    assert ans1 == 2660
    assert ans2 == 1256
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
