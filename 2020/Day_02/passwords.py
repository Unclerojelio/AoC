f = open("input.txt", "r")
lines = f.readlines()

#lines = ['1-3 a: abcde', '1-3 b: cdefg',  '2-9 c: ccccccccc']

count1 = 0
count2 = 0
for line in lines:
    line = line.strip()
    a, b, password = line.split(" ")
    at_least, at_most = a.split("-")
    letter = b[0]
    occurs = password.count(letter)
    if occurs >= int(at_least) and occurs <= int(at_most):
        count1 += 1

    first = at_least
    second = at_most
    operand1 = not (password[int(first) - 1] == letter) and password[int(second) - 1] == letter
    operand2 = password[int(first) - 1] == letter and not password[int(second) - 1] == letter
    if operand1 or operand2:
        count2 += 1
print(f"Part 1: {count1} Part 2: {count2}")