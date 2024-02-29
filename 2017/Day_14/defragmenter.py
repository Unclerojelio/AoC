import time
import functools

def do_tests():
    line = 'flqrgnkx'
    ans1, ans2 = solve(line)
    assert ans1 == 8108
    # assert ans2 == 10
    return True

def count_bits(row):
    return 0

def knot_hash(line):
    num_elements = 256
    lengths = []
    for ch in line:
        lengths.append(ord(ch))
    lengths = lengths + [17,31,73,47,23]

    skip = 0
    position = 0
    elements = list(range(num_elements))
    for _ in range(64):
        for length in lengths:
            if position + length  <= num_elements:
                substr = elements[position:position + length]
                substr = substr[::-1]
                elements = elements[:position] + substr + elements[position + length:]
            else:
                substr = elements[position:] + elements[:(position + length) - num_elements]
                substr = substr[::-1]
                elements = substr[num_elements - position:] + elements[position + length - num_elements: position] + substr[:num_elements - position]
            position = (position + length + skip) % num_elements
            skip += 1
    substrings = [elements[i:i + 16] for i in range(0, len(elements), 16)]
    dense_hash = []

    for substr in substrings:
        dense_hash.append(functools.reduce(lambda x, y: x ^ y, substr))

    hex_string = ''
    for num in dense_hash:
        num = hex(num)[2:]
        if len(num) == 1:
            num = '0' + num
        hex_string = hex_string + num

    return hex_string

def solve(line):
    ans1, ans2 = 0,0
    for i in range(128):
        row = knot_hash(line + '-' + str(i))
        ans1 += count_bits(row)
        print(row)
    return ans1, ans2

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    line = 'ugkiagan'
    ans1, ans2 = solve(line)
    
    # assert ans1 == 1900
    # assert ans2 == 3966414
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
