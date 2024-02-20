import time

def do_tests(display):
    lines = ''''''
    lines = lines.splitlines()
    for line in lines:
        instruction = parse(line)
        update(display, instruction)

    # assert ans1 == "easter"
    # assert ans2 == "advent"
    return True

def parse(line):
    tokens = line.split()
    if tokens[0] == 'rect':
        x, y = tokens[1].split('x')
        return (tokens[0], int(x), int(y))
    else:
        start = int(tokens[2].split('=')[1])
        delta = int(tokens[4])
        return (tokens[1], start, delta)


def update(display, instruction):
    if instruction[0] == 'rect':
        print(instruction)
        for y in range(instruction[2]):
            x = instruction[1]
            str = '#' * x
            display[y] = str + display[y][x:]
    return display

def main():
    start_time = time.time()

    # length of test data is different than input data. 
    # if do_tests():
    #     print("Tests Passed")

    ans1 = 0
    ans2 = 0
    display = ['.' * 50 for _ in range(6)]
    lines = open(0).read().splitlines()
    for line in lines:
        instruction = parse(line)
        update(display, instruction)
    
    for y in range(len(display)):
        for x in range(len(display[0])):
            if display[y][x] == '#':
                ans1 += 1

    for y in range(len(display)):
        print(display[y])
    
    # assert ans1 == "umejzgdw"
    # assert ans2 == "aovueakv"
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()