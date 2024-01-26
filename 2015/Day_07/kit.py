import time

wires = {}

def evaluate(wire):
    #print(wire)
    if wire[0].isdigit():
        print(int(wire[0]))
        return int(wire[0])
    elif 'NOT' in  wire:
        evaluate(wire[1]) ^ 0b1111111111111111
    elif 'RSHIFT' in wire:
        evaluate(wire[0]) >> int(wire[2])
    elif 'LSHIFT' in wire:
        evaluate(wire[0]) << int(wire[2])
    elif 'AND' in wire:
        #print(wire[0], wire[2])
        evaluate(wire[0]) & evaluate(wire[2])
    elif 'OR' in wire:
        evaluate(wire[0]) | evaluate(wire[2])
    else:
        return wire[0]


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
    v, k = line.split(' -> ')
    wires[k] = v.split()
    #print(k, wires[k])

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
