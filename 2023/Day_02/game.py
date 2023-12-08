import sys

lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]

number = []
total = 0

for line in lines:
    games = []
    attempts = []
    line = line[4:]
    index = line.find(":")
    number = line[:index]
    line = line[index+2:]
    line = line.split(';')
    for game in line:
        games.append(game.split(','))
    for game in games:
        pulls = []
        for cubes in game:
            cubes = cubes.strip().split()
            pulls.append(cubes)
        attempts.append(pulls)
    for attempt in attempts:
        result = False
        red_result = False
        green_result = False
        blue_result = False
        for pull in attempt:
            print(pull)
            if pull[1] == 'red' and int(pull[0]) <= 12:
                red_result = True
            if pull[1] == 'green' and int(pull[0]) <= 13:
                green_result = True
            if pull[1] == 'blue' and int(pull[0]) <= 14:
                blue_result = True
        result = red_result and green_result and blue_result
        if result:
            total += int(number)
print(number)