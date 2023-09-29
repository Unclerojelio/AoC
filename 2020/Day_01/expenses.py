f = open("input2.txt", "r")
lines = f.readlines()

lines = [int(line) for line in lines]

for i in range(0, len(lines) - 1):
    for j in range(i, len(lines) - 1):
        for k in range(j, len(lines) - 1):
            if (lines[i] + lines[j] + lines[k]) == 2020:
                print(lines[i] * lines[j] * lines[k])