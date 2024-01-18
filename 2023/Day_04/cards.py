# Thanks to HyperNeutrino on YouTube

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

m = {}
for i, card in enumerate(cards):
    if i not in m:
        m[i] = 1
    for _ in range(card[3]):
        count = 0
        for choice in card[2]:
            if choice in card[1]:
                count += 1
    for index in range(i + 1, i + count + 1):
        m[index] = m.get(index, 1) + m[i]

ans2 = 0
for i in range(len(m)):
    ans2 += m[i]

assert sum == 24160
assert ans2 == 5659035
print(f"The answer for Part 1: {sum}, The answer for Part 2: {ans2}")

end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")