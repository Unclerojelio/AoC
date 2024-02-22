import time

def do_tests():
    line = '''0 2 7 0'''
    blocks = line.split()
    blocks = [int(item) for item in blocks]
    ans1, ans2 = solve(blocks)

    assert ans1 == 5
    assert ans2 == 4
    return True

def solve(blocks):
    states = []
    while True:
        largest = max(blocks)
        largest_index = blocks.index(largest)
        blocks[largest_index] = 0
        while largest > 0:
            largest_index = (largest_index + 1) % len(blocks)
            blocks[largest_index] += 1
            largest -= 1
        block_str = ' '.join(str(n) for n in blocks)
        if block_str not in states:
            states.append(block_str)
        else:
            pos = states.index(block_str)
            return len(states) + 1, len(states) - pos

def main():
    start_time = time.time()
 
    if do_tests():
        print("Tests Passed")

    line = open(0).read()
    blocks = line.split()
    blocks = [int(item) for item in blocks]
    ans1, ans2 = solve(blocks)
    
    assert ans1 == 12841
    assert ans2 == 8038
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
