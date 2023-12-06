import sys

lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]

number = []
for line in lines:
    line = line[4:]
    index = line.find(":")
    number = line[:index]
    line = line[index+2:]
    print(int(number), line)