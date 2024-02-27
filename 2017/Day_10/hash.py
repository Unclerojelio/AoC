import time
import functools

def do_tests():
    num_elements = 5
    line = [3, 4, 1, 5]
    ans1 = solve(line, num_elements)
    assert ans1 == 12
    ans2 = solve2('3,4,1,5', 256)
    assert ans2 == '4a19451b02fb05416d73aea0ec8c00c0'
    ans2 = solve2('', 256)
    assert ans2 == 'a2582a3a0e66e6e86e3812dcb672a272'
    return True

def solve(line, num_elements):
    skip = 0
    position = 0
    elements = list(range(num_elements))
    for length in line:
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
        assert len(elements) == num_elements

    ans1 = elements[0] * elements[1]
    return ans1

def solve2(line, num_elements):
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

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")
    
    bytestr = open(0).read().strip()
    line = [int(x) for x in bytestr.split(',')]
    num_elements = 256
    ans1 = solve(line, num_elements)
    ans2 = solve2(bytestr, num_elements)
    
    assert ans1 == 212
    assert ans2 == '96de9657665675b51cd03f0b3528ba26'
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
