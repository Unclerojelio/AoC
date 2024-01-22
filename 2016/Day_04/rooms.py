import time

start = time.time()

lines = open(0).read().splitlines()
ans1 = 0
rooms = []
for line in lines:
    name = ""
    first = line.split('-')
    last = first[-1:]
    first = first[:-1]
    for part in first:
        name += part
    sector, checksum = last[0].split('[')
    checksum = checksum[:-1]
    #print(name, sector, checksum)
    letters = {}

    for letter in name:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    sorted_letters = dict(sorted(letters.items(), key=lambda item: (-item[1], item[0])))
    letters = ""
    for letter in sorted_letters:
        letters += letter

    if letters[:5] == checksum:
        ans1 += int(sector)
    rooms.append((name, int(sector)))
assert ans1 == 278221
print(ans1)
names = []
for room, sector in rooms:
    name = ""
    for c in room:
        name = name + chr((ord(c) - 97 + sector)%26 + 97)
    names.append(name)
    x = name.find('north')
    if x != -1:
        ans2 = sector
assert ans2 == 267
print(ans2)


end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")