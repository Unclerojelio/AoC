f = open("input.txt", "r")
lines = f.readlines()

#lines = ['14', '1969', '100756']

sum = 0
for line in lines:
    #print(line)
    fuel = int(line) // 3 - 2
    #print(fuel)
    sum += fuel
    while fuel >= 0:
        fuel = fuel // 3 - 2
        #print(fuel)
        if fuel > 0:
            sum += fuel

print(sum)
