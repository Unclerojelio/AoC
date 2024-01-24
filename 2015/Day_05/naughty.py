import re

f = open("input.txt", "r")
#lines = f.readlines()
lines = [line.rstrip() for line in f.readlines()]

#Part 1 test set
#lines = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']

#Part 2 test set
#lines = ['aaaa', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

#doubles = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo','pp','qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

def has_bad_words(line):
    bad_words = ["ab", "cd", "pq", "xy"]
    for bad_word in bad_words:
        if bad_word in line:
            #print(f"This line has a bad word:  {line}")
            return True
    #print(f"This line does not have a bad word:  {line}")
    return False

def has_vowels(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for vowel in vowels:
        if vowel in line:
            count += line.count(vowel)
    if count >= 3:
        #print(f"This line has three vowels:  {line} Count: {count}")
        return True
    #print(f"This line does not have three vowels:  {line} Count: {count}")
    return False

def has_doubles(line):
    doubles = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo','pp','qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
    for double in doubles:
        if double in line:
            #print(f"This line has a double:  {line}")
            return True
    #print(f"This line does not have a double:  {line}")
    return False

def appears_twice(line):
    if len(line) < 4:
        return False
    while len(line) >= 4:
        l1 = line[0]
        l2 = line[1]
        line = line[1:]
        if line.find(''.join([l1, l2]), 1) > 0:
            #print(''.join([l1, l2]))
            return True
    return False

def two_separated_letters(line):
    if len(line) < 3:
        return False
    while len(line) >= 3:
        letters = line[:3]
        letter1 = letters[0]
        letter2 = letters[1]
        letter3 = letters[2]
        if letter1 == letter3:
            #print(''.join([letter1, letter2, letter3]))
            return True
        line = line[1:]
    return False

ans1 = 0
ans2 = 0
for line in lines:
    if not has_bad_words(line) and has_vowels(line) and has_doubles(line):
        ans1 += 1
    if appears_twice(line) and two_separated_letters(line):
        #print(line, "Nice")
        ans2 += 1
    # else:
    #     print(line, "Naughty")

#assert count == 3
assert ans2 == 69
assert ans1 == 238
print(f"Part 1 answer: {ans1} Part 2 answer: {ans2}")
