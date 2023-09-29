import pprint
import sys

lines = sys.stdin.readlines()

# lines = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
#          'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#          'bright white bags contain 1 shiny gold bag.',
#          'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#          'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#          'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#          'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#          'faded blue bags contain no other bags.',
#          'dotted black bags contain no other bags.']

lines = [line.rstrip() for line in lines]

#print(lines)

def traverse(graph, bag, visited):
    count = 1

    if bag in visited:
        return 0
    else:
        visited.append(bag)

    if bag not in graph:
        #print(bag)
        return 1
    else:
        for bag in graph[bag]:
            #print(bag)
            count += traverse(graph, bag, visited)
        return count

containers = []
for line in lines:
    container, containees = line.split('contain')
    container = container[:-6]
    if containees[1:3] == 'no':
        containees = []
    else:
        containees = containees.split(',')
        for i in range(len(containees)):
            containees[i] = containees[i][3:]
            containees[i] = containees[i].split(' ')
            containees[i] = containees[i][0] + ' ' + containees[i][1]
    containers.append([container, containees])
#pprint.pprint(containers)

graph = {}
for container in containers:
    for bag in container[1]:
        if bag not in graph:
            graph[bag] = [container[0]]
        else:
            graph[bag].append(container[0])

#pprint.pprint(graph)
visited = []
print(f"Part 1: {traverse(graph, 'shiny gold', visited) - 1} Part 2: ")
#pprint.pprint(visited)