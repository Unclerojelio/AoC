import time

def do_tests():
    num_elements = 5
    line = [3, 4, 1, 5]
    ans1, ans2 = solve(line, num_elements)
    assert ans1 == 12
    #assert ans2 == 10
    return True

def solve(line, num_elements):
    skip = 0
    position = 0
    elements = list(range(num_elements))
    #print(elements)
    for length in line:
        if position + length  <= num_elements:
            substr = elements[position:position + length]
            substr = substr[::-1]
            elements = elements[:position] + substr + elements[position + length:]
            #print(substr, elements)
        else:
            substr = elements[position:] + elements[:(position + length) - num_elements]
            substr = substr[::-1]
            #print(substr[num_elements - length + 1:], elements[position + length - num_elements: position], substr[:num_elements - position], position, length)
            elements = substr[num_elements - position:] + elements[position + length - num_elements: position] + substr[:num_elements - position]
            #print(substr, elements)
        position = (position + length + skip) % num_elements
        skip += 1
        #print(length, position, skip)
        #print(elements)
        assert len(elements) == num_elements

    ans1 = elements[0] * elements[1]
    ans2 = 0
    return ans1, ans2


def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    line = [int(x) for x in open(0).read().strip().split(',')]
    num_elements = 256
    ans1, ans2 = solve(line, num_elements)
    
    assert ans1 == 212
    #assert ans2 == 7284
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
