import time
from collections import defaultdict

def do_tests():
    lines = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''
    lines = lines.splitlines()
    ans1, ans2 = solve(lines)

    assert ans1 == 'tknk'
    #assert ans2 == 4
    return True

def dfs(children, weights, root):
    exp = None
    s = weights[root]
    for child in children[root]:
        w = dfs(children, weights, child)
        s += w
        if exp is None:
            exp = w
        elif exp != w:
            print('expected child ', child, weights[child], ' to have weight ', exp, ' has weight ', w)
    return s

def parse(lines):
    programs = {}
    for line in lines:
        if ' -> ' in line:
            pos = line.find(' -> ')
            name = line[:pos]
            children = line[pos+4:]
            children = children.split(', ')
        else:
            name = line
            children = []
        pos = name.find('(')
        weight = int(name[pos+1:-1])
        name = name[:pos-1]
        programs[name] = [weight, children]
    return programs
    

def solve(lines):
    ans2 = 0
    programs = parse(lines)

    leaves = set()
    children = defaultdict(list)
    weights = {}
    for program in programs:
        weights[program] = programs[program][0]
        if programs[program][1] != []:
            children[program] = programs[program][1]
            for child in programs[program][1]:
                leaves.add(child)
    for program in programs:
        if program not in leaves:
            ans1 = program

    dfs(children, weights, ans1)

    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    ans1, ans2 = solve(lines)
    
    assert ans1 == 'rqwgj'
    # assert ans2 == 8038
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
