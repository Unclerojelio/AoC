import time
import re

def getNumbers(line):
    numbers = re.findall(r'-?[0-9]+', line)
    return numbers

start_time = time.time()
ans1 = 0
json_doc = open(0).read()
lines = json_doc.split(',')
for line in lines:
    ans1 += sum([int(i) for i in getNumbers(line)])
# line = r'{"a":2"b":4}'
# line = r'[[[3]]]'
# line = r'{"a":{"b":4},"c":-1}'
# line = r'{"a":[-1,1]}'
#line = r'{"e":[[{"e":86,"c":23,"a":{"a":[120,169,"green","red","orange"],"b":"red"},"g":"yellow","b":["yellow"],"d":"red","f":-19},{"e":-47,"a":[2],"d":{"a":"violet"},"c":"green","h":"orange",' 
#ans1 = sum([int(i) for i in getNumbers(line)])
assert ans1 == 111754
print(ans1)

stack = []
for ch in json_doc:
    print(stack)
    if ch == '[' or ch == '{':
        stack.append(ch)
    elif ch == ']' or ch == '}':
        if len(stack) == 0:
            print("False")
        elif ch == stack[-1]:
            stack.pop()
if len(stack) == 0:
    print("True")
else:
    print("False")
    
    


print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")
