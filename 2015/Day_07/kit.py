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

ans1 = evaluate('a')
assert ans1 == 46065
mem = {}
wires['b'] = ['46065']
ans2 = evaluate('a')
assert ans2 == 14134
print(f"Answer 1: {ans1} Answer 2: {ans2}")
print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")
