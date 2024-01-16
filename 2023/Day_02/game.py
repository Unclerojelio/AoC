import sys
import time

start = time.time()

lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]

number = []
total = 0
power_sum = 0

for line in lines:
    game_result = True
    min_red = 0
    min_green = 0
    min_blue = 0
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
        result = True
        red_result = True
        green_result = True
        blue_result = True
        for pull in attempt:
            if pull[1] == 'red':
                if int(pull[0]) > min_red:
                    min_red = int(pull[0])
            if pull[1] == 'green':
                if int(pull[0]) > min_green:
                    min_green = int(pull[0])
            if pull[1] == 'blue':
                if int(pull[0]) > min_blue:
                    min_blue = int(pull[0])
            if pull[1] == 'red' and int(pull[0]) > 12:
                red_result = False
            if pull[1] == 'green' and int(pull[0]) > 13:
                green_result = False
            if pull[1] == 'blue' and int(pull[0]) > 14:
                blue_result = False
        result = red_result and green_result and blue_result
        #print(f"Attempt: {attempt} Result: {result}")
        game_result = game_result and result
    #print(f"Game result: {game_result}")
    if game_result:
        total += int(number)
    power_sum += min_red * min_green * min_blue
assert total == 2406
assert power_sum == 78375
print(f"Day 1 answer: {total} Day 2 answer: {power_sum}") #2406 is correct, 78375 is correct

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")