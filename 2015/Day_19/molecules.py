import time
import re
from itertools import combinations
from queue import Queue
from queue import PriorityQueue
import math

def parse_file(lines):
    replacements = []
    starting_molecule = lines[-1]
    lines = lines[:-2]
    for line in lines:
        k, v = line.split('=>')
        k = k.strip()
        v = v.strip()
        replacements.append((k, v))
    return replacements, starting_molecule

def get_neighbors(replacements, molecule):
    for new, old in replacements:
        for i in range(len(molecule) - len(old) + 1):
            if molecule[i:i + len(old)] == old:
                yield molecule[:i] + new + molecule[i + len(old):]

def bfs(replacements, start, goal):
    q = Queue()
    q.put(start)
    dist = {start :0}

    while not q.empty():
        current = q.get()
        if current == goal:
            return dist[current]
        
        for neighbor in get_neighbors(replacements, current):
            if neighbor in dist:
                continue
            dist[neighbor] = dist[current] + 1
            q.put(neighbor)

def astar(replacements, start, goal):
    def h(x):
        return int(math.ceil((len(x) - 1) / 9))
    
    q = PriorityQueue()
    q.put((h(start), start))
    #print(q.get())
    dist = {start :0}

    while not q.empty():
        _,current = q.get()
        if current == goal:
            return dist[current]
        
        for neighbor in get_neighbors(replacements, current):
            tentative_dist = dist[current] + 1
            if neighbor not in dist or tentative_dist < dist[neighbor]:
                dist[neighbor] = tentative_dist
                q.put((h(neighbor), neighbor))

def solve(replacements, starting_molecule):
    molecules = set()
    for replacement in replacements:
        positions = [i.start() for i in re.finditer(replacement[0], starting_molecule)]
        for position in positions:
            head = starting_molecule[:position]
            if position + len(replacement[0]) >= len(starting_molecule):
                tail = ''
            else:
                tail = starting_molecule[position+len(replacement[0]):]
            molecules.add(head + replacement[1] + tail)
    #ans1 = len(molecules)
    return len(molecules)

def do_tests():
    lines = '''e => H
    e => O
    H => HO
H => OH
O => HH

HOH'''
    lines = lines.splitlines()
    replacements, starting_molecule = parse_file(lines)
    ans1 = solve(replacements, starting_molecule)
    ans2 = bfs(replacements, starting_molecule, 'e')
    ans3 = astar(replacements, starting_molecule, 'e')
    assert ans1 == 4
    assert ans2 == 3
    assert ans3 == 3

    lines = '''e => H
    e => O
    H => HO
H => OH
O => HH

HOHOHO'''
    lines = lines.splitlines()
    replacements, starting_molecule = parse_file(lines)
    ans1 = solve(replacements, starting_molecule)
    ans2 = bfs(replacements, starting_molecule, 'e')
    ans3 = astar(replacements, starting_molecule, 'e')
    assert ans1 == 7
    assert ans2 == 6
    assert ans3 == 6
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    replacements, starting_molecule = parse_file(open(0).read().splitlines())
    ans1 = solve(replacements, starting_molecule)
    ans2 = astar(replacements, starting_molecule, 'e')

    assert ans1 == 518
    assert ans2 == 200
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
