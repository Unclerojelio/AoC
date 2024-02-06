import time
import re
from itertools import combinations

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

def solve(replacements, starting_molecule):
    molecules = set()
    answer = len(molecules)
    return answer

def do_tests():
    lines = '''H => HO
H => OH
O => HH

HOH'''
    lines = lines.splitlines()
    replacements, starting_molecule = parse_file(lines)
    ans1 = solve(replacements, starting_molecule)
    #ans2 = solve()

    assert ans1 == 0
    # assert ans2 == 
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    replacements, starting_molecule = parse_file(open(0).read().splitlines())
    print(replacements)
    ans1 = solve(replacements, starting_molecule)
    #ans2 = solve()

    ans2 = 0
    assert ans1 == 0
    # assert ans2 == 
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()