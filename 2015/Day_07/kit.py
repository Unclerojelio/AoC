import time

wires = {}

def evaluate(wire):
    print(wire)
    if len(wire) == 1:
        if wire[0].isdigit():
            return int(wire[0])
        else:
            return evaluate(wires[wire[0]])
    elif len(wire) == 2:
        return evaluate(wires[wire[1]]) ^ 0b1111111111111111
    elif len(wire) == 3:
        if wire[1] == "RSHIFT":
            return evaluate(wires[wire[0]]) >> evaluate([wire[2]])
        elif wire[1] == "LSHIFT":
            return evaluate(wires[wire[0]]) << evaluate([wire[2]])
        elif wire[1] == "AND":
            if wire[0].isdigit():
                return evaluate(wire[0]) & evaluate(wires[wire[2]])
            elif wire[2].isdigit():
                return evaluate(wires[wire[0]]) & evaluate(wire[2])
            else:
                return evaluate(wires[wire[0]]) & evaluate(wires[wire[2]])
        elif wire[1] == "OR":
            if wire[0].isdigit():
                return evaluate(wire[0]) | evaluate(wires[wire[2]])
            elif wire[2].isdigit():
                return evaluate(wires[wire[0]]) | evaluate(wire[2])
            else:
                return evaluate(wires[wire[0]]) | evaluate(wires[wire[2]])
        else:
            print(f"Unexpected line: {wire}")


start_time = time.time()
lines = open(0).read().splitlines()

lines = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
111 -> j
j -> x'''
lines = lines.splitlines()

for line in lines:
    #print(line)
    tokens = line.split()
    wires[tokens[-1:][0]] = tokens[:-2]

wires['d'] = evaluate(wires['d'])
wires['e'] = evaluate(wires['e'])
wires['f'] = evaluate(wires['f'])
wires['g'] = evaluate(wires['g'])
wires['h'] = evaluate(wires['h'])
wires['i'] = evaluate(wires['i'])
wires['x'] = evaluate(wires['x'])
wires['y'] = evaluate(wires['y'])
#wires['a'] = evaluate(wires['a'])
#print(wires['a'])
for wire in wires:
    print(wire, wires[wire])




print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")
