f = open("2017/Day_02/input.txt", "r")
lines = f.readlines()

values = []
sum = 0
sum2 = 0
for line in lines:
    values = line.rstrip().split('\t')
    values = [int(value) for value in values]
    sum += max(values) - min(values)
    for i in range(len(values)-1):
        for j in range(i+1, len(values)):
            dividend = max(values[i], values[j])
            divisor = min(values[i], values[j])
            if dividend % divisor == 0:
                sum2 += dividend // divisor

print(f"Part 1: {sum}")
print(f"Part 2: {sum2}")