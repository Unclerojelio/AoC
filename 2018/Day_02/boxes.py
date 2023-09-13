f = open("2018/Day_02/input.txt", "r")
lines = f.readlines()

#lines = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

letters = "abcdefghijklmnopqrstuvwxyz"
doubles = 0
triples = 0
double_flag = False
triple_flag = False
for line in lines:
    for letter in letters:
        occurs = line.count(letter)
        if occurs == 2:
            double_flag = True
        elif occurs == 3:
            triple_flag = True
    if double_flag:
        doubles += 1
    if triple_flag:
        triples += 1
    double_flag = False
    triple_flag = False
count = 0
output = ''
for i in range(len(lines)-1):
    for j in range(i, len(lines)):
        for k in range(len(lines[i])):
            if lines[i][k] == lines[j][k]:
                count += 1
        if count == len(lines[i]) - 1:
            for l in range(len(lines[i])):
                if lines[i][l] == lines[j][l]:
                    output += lines[i][l]
            #print(lines[i])
            #print(lines[j])
        count = 0

print(f"Part 1: {doubles * triples} Part 2: {output}")
