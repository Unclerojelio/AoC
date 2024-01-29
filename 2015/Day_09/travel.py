import time
from itertools import permutations

def solve():
    ans1 = 0
    ans2 = 0
    routes = []
    towns = set()
    distances = {}
    totals = set()
    lines = open(0).read().splitlines()
    for line in lines:
        l, distance = line.split(" = ")
        town1, town2 = l.split(" to ")
        towns.add(town1)
        towns.add(town2)
        distances[town1+town2] = int(distance)
        distances[town2+town1] = int(distance)
        
    routes = permutations(towns)
    for route in routes:
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[route[i] + route[i+1]]
            #print(route[i] + route[i+1], distance)
        totals.add(distance)
    ans1 = min(totals)
    ans2 = max(totals)

    return [ans1, ans2]

def main():
    start = time.time()

    ans1, ans2 = solve()
    assert ans1 == 141
    assert ans2 == 736
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    end = time.time()
    print("Elapsed time:", (end-start) * 10**3, "ms")


if __name__=="__main__":
    main()
