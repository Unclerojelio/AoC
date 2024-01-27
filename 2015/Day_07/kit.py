import time

wires = {}
mem = {}

def evaluate(k):
    if k in mem:
        return mem[k]
    if k.isdigit(): 
        return int(k)
    v = wires[k]
    if 'NOT' in  v:
        result = evaluate(v[1]) ^ 0b1111111111111111
        mem[k] = result
        return result
    elif 'RSHIFT' in v:
        result = evaluate(v[0]) >> int(v[2])
        mem[k] = result
        return result
    elif 'LSHIFT' in v:
        result = evaluate(v[0]) << int(v[2])
        mem[k] = result
        return result
    elif 'AND' in v:
        result = evaluate(v[0]) & evaluate(v[2])
        mem[k] = result
        return result
    elif 'OR' in v:
        result = evaluate(v[0]) | evaluate(v[2])
        mem[k] = result
        return result
    result = evaluate(v[0])
    mem[k] = result
    return result


start_time = time.time()
lines = open(0).read().splitlines()

for line in lines:
    v, k = line.split(' -> ')
    wires[k] = v.split()  

wires['a'] = evaluate('a')
assert wires['a'] == 46065
print(wires['a'])
#part 2 14134
print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")
