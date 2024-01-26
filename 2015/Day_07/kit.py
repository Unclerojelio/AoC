import time

wires = {}

def evaluate(k):
    if len(wires[k]) == 1 and wires[k][0].isdigit():
        return int(wires[k][0])
    print(k, wires[k])
    # if wire[0].isdigit():
    #     wires[wire[2]] = int(wire[0])
    #     return int(wire[0])
    if 'NOT' in  wires[k]: # This is returning an int which is not an iterable.
        wires[k] = evaluate(wires[k]) ^ 0b1111111111111111
        return wires[k]
    elif 'RSHIFT' in wires[k]:
        wires[k] = evaluate(wires[k][0]) >> int(wires[k][2])
        return wires[k]
    elif 'LSHIFT' in wires[k]:
        wires[k] = evaluate(wires[k][0]) << int(wires[k][2])
        return wires[k]
    elif 'AND' in wires[k]:
        wires[k] = evaluate(wires[k][0]) & evaluate(wires[k][2])
        return wires[k]
    elif 'OR' in wires[k]:
        wires[k] = evaluate(wires[k][0]) | evaluate(wires[k][2])
        return wire[k]
    else:
        if wires[k][0].isdigit():
            wires[k] = int(wires[k][0])
        else:
            wires[k] = evaluate(wires[k][0])
        return wires[k]


start_time = time.time()
lines = open(0).read().splitlines()

# lines = '''123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# 111 -> j
# j -> x'''
# lines = lines.splitlines()

for line in lines:
    v, k = line.split(' -> ')
    wires[k] = v.split()
    #print(k, wires[k])   

# wires['d'] = evaluate(wires['d'])
# wires['e'] = evaluate(wires['e'])
# wires['f'] = evaluate(wires['f'])
# wires['g'] = evaluate(wires['g'])
# wires['h'] = evaluate(wires['h'])
# wires['i'] = evaluate(wires['i'])
# wires['x'] = evaluate(wires['x'])
# wires['y'] = evaluate(wires['y'])
# for wire in wires:
#     print(wire, wires[wire])

#160 is too low
wires['a'] = evaluate('a')
print(wires['a'])


print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")
