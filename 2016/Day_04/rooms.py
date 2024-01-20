import time

start = time.time()

lines = open(0).read().splitlines()
ans1 = 0
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

    sorted_letters = dict(reversed(sorted(letters.items(), key=lambda item: item[1])))
    letters = ""
    for letter in sorted_letters:
        letters += letter

    if letters[:5] == checksum:
        ans1 += int(sector)
print(ans1)


end = time.time()
print("Elapsed time:", (end-start) * 10**3, "ms")