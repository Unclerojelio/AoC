import time

start = time.time()

lines = open(0).read().splitlines()
sum = 0
cards = []
card_num = 0
for line in lines:
    card_num += 1
    index = line.find(":")
    line = line[index+1:]
    winners, choices = line.split("|")
    winners = winners.split()
    choices = choices.split()
    count = 0
    for choice in choices:
        if choice in winners:
            count += 1
    if count >= 1:
        sum += 2**(count - 1)

    cards.append([card_num, winners, choices, 1])

ans2 = 0
for card in cards:
    for _ in range(card[3]):
        count = 0
        for choice in card[2]:
            if choice in card[1]:
                count += 1
        for index in range(count):
            cards[card[0] + index][3] += 1
    ans2 += card[3]

assert sum == 24160
assert ans2 == 5659035
print(f"The answer for Part 1: {sum}, The answer for Part 2: {ans2}")

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")