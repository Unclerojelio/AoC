import time
import re

def extract_substrings(string):
    pattern = r'\[([^\]]+)\]|([^[\]]+)'
    matches = re.findall(pattern, string)
    substrings_inside_brackets = [match[0] for match in matches if match[0]]
    substrings_outside_brackets = [match[1] for match in matches if match[1]]
    return substrings_inside_brackets, substrings_outside_brackets

def has_special_pattern(substrings):
    for substring in substrings:
        for i in range(len(substring) - 3):
            if (substring[i] != substring[i + 1] and
                substring[i] == substring[i + 3] and
                substring[i + 1] == substring[i + 2]):
                return True
    return False

def do_tests():
    lines = '''abba[mnop]qrst
    abcd[bddb]xyyx
    aaaa[qwer]tyui
    ioxxoj[asdfgh]zxcvbn'''
    lines = lines.splitlines()
    addresses = parse_file(lines)
    ans1, ans2 = solve(addresses)

    assert ans1 == 2
    # assert ans2 == "advent"
    return True

def parse_file(lines):
    addresses = lines
    return addresses


def solve(addresses):
    ans1 = 0
    ans2 = 0
    for address in addresses:
        substrings_inside_brackets, substrings_outside_brackets = extract_substrings(address)
        if not has_special_pattern(substrings_inside_brackets) and has_special_pattern(substrings_outside_brackets):
            ans1 += 1
        
    return ans1, ans2

def main():
    start_time = time.time()

    if do_tests():
        print("Tests Passed")

    lines = open(0).read().splitlines()
    addresses = parse_file(lines)
    ans1, ans2 = solve(addresses)
    
    assert ans1 == 115
    # assert ans2 == "aovueakv"
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()