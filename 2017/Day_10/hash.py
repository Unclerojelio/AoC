import time

def do_tests():
    num_elements = 5
    line = [3, 4, 1, 5]
    ans1, ans2 = solve(line, num_elements)
    assert ans1 == 0
    #assert ans2 == 10
    return True

def solve(line, num_elements):
    elements = []
    skip = 0
    for i in range(num_elements):
        elements.append(i)

    position = 0
    for length in line:
        position = (position + length + skip) % num_elements
        skip += 1
        print(length, position, skip)

    print(line)
    print(elements)

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
    
    #assert ans1 == 16869
    #assert ans2 == 7284
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
