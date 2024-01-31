import time
import re

def sum_nums(line):
    numbers = re.findall(r'-?[0-9]+', line)
    return sum(map(int, numbers))

def is_balanced(line):
    stack = []
    for ch in line:
        if ch == '[' or ch == '{':
            stack.append(ch)
        elif ch == ']' or ch == '}':
            if len(stack) == 0:
                return False
            elif (stack[-1] == '{' and ch == '}') or (stack[-1] == '[' and ch == ']'):
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def parse_line(line):
    stack = []
    for ch in line:
        temp = ''
        if ch == ']':
            while stack[-1] != '[':
                temp = stack.pop() + temp
            stack.pop()
            stack.append(str(sum_nums(temp)))
        elif ch == '}':
            while stack[-1] != '{':
                temp = stack.pop() + temp
            stack.pop()
            if temp.find('red') == -1:
                stack.append(str(sum_nums(temp)))
        else:
            stack.append(ch)
    return stack
    
def do_tests():
    assert sum_nums(r'[1,2,3]') == 6
    assert sum_nums(r'{"a":2"b":4}') == 6
    assert sum_nums(r'[[[3]]]') == 3
    assert sum_nums(r'{"a":{"b":4},"c":-1}') == 3
    assert sum_nums(r'{"a":[-1,1]}') == 0
    assert sum_nums(r'[-1,{"a":1}]') == 0
    assert sum_nums(r'[-1,{"a":2}]') != 0

    assert is_balanced(r'[1,2,3]') == True
    assert is_balanced(r'{"a":2"b":4}') == True
    assert is_balanced(r'[[[3]]]') == True
    assert is_balanced(r'{"a":{"b":4},"c":-1}') == True
    assert is_balanced(r'{"a":[-1,1]}') == True
    assert is_balanced(r'[-1,{"a":1}]') == True
    assert is_balanced(r'[-1,{"a":1}}') == False
    
    assert sum(map(int, parse_line(r'[1,2,3]'))) == 6
    assert sum(map(int, parse_line(r'{"a":2"b":4}'))) == 6
    assert sum(map(int, parse_line(r'[[[3]]]'))) == 3
    assert sum(map(int, parse_line(r'{"a":{"b":4},"c":-1}'))) == 3
    assert sum(map(int, parse_line(r'{"a":[-1,1]}'))) == 0
    assert sum(map(int, parse_line(r'[-1,{"a":1}]'))) == 0
    assert sum(map(int, parse_line(r'[-1,{"a":2}]'))) != 0
    assert sum(map(int, parse_line(r'[1,{"c":"red","b":2},3]'))) == 4
    assert sum(map(int, parse_line(r'{"d":"red","e":[1,2,3,4],"f":5}'))) == 0
    assert sum(map(int, parse_line(r'[1,"red",5]'))) == 6

    return True

def main():
    start_time = time.time()

    if do_tests():
        print("Tests Passed")

    json_doc = open(0).read()
    ans1 = sum_nums(json_doc)
    ans2 = sum(map(int, parse_line(json_doc)))
    assert ans1 == 111754
    assert ans2 == 65402
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
