import pprint
import sys

def do_move(x, y, move, keypad):
    return x, y

lines = sys.stdin.readlines()

# lines = ["ULL", 
         # "RRDDD",
         # "LURDL",
         # "UUUUD"]
         
keypad = ["123",
          "456",
          "789"]
          
keypad2 = [['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '1', '0', '0', '0'],
           ['0', '0', '2', '3', '4', '0', '0'],
           ['0', '5', '6', '7', '8', '9', '0'],
           ['0', '0', 'A', 'B', 'C', '0', '0'],
           ['0', '0', '0', 'D', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0']]

lines = [line.rstrip() for line in lines]

x = 1
y = 1
start = keypad[y][x]
output = ''

for line in lines:
    for move in line:
        if move == 'U':
            y -= 1
            if y < 0:
                y = 0
                
        elif move == 'D':
            y += 1
            if y > 2:
                y = 2
                
        elif move == 'L':
            x -= 1
            if x < 0:
                x = 0
                
        elif move == 'R':
            x += 1
            if x > 2:
                x = 2
                
    #print(keypad[y][x])
    output += keypad[y][x]
print(output)
                