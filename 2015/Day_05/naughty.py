import re

f = open("input.txt", "r")
#lines = f.readlines()
lines = [line.rstrip() for line in f.readlines()]

#lines = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']

doubles = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo','pp','qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

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
    for double in doubles:
        if double in line:
            #print(f"This line has a double:  {line}")
            return True
    #print(f"This line does not have a double:  {line}")
    return False

nice_list = []
for line in lines:
    if not has_bad_words(line) and has_vowels(line) and has_doubles(line):
        nice_list.append(line)
        #print(line)
assert len(nice_list) == 238
print(len(nice_list))

lines = ['aaaa', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

def appears_twice(line):
    print(f"Received by twice: {line}")
    if len(line) < 4:
        return False
    while len(line) >= 4:
        l1 = line[0]
        l2 = line[1]
        line = line[1:]
        if line.find(''.join([l1, l2])) > 0:
            #print(''.join([l1, l2]))
            return True
        #line = line[1:]
    return False

def two_separated_letters(line):
    print(f"Received by separated: {line}")
    if len(line) < 3:
        return False
    while len(line) >= 3:
        letters = line[:3]
        #print(letters)
        #print(line)
        letter1 = letters[0]
        letter2 = letters[1]
        letter3 = letters[2]
        if letter1 == letter3:
            #print(''.join([letter1, letter2, letter3]))
            return True
        line = line[1:]
    return False

count = 0
for line in lines:
    if appears_twice(line) and two_separated_letters(line):
        print(line, "Nice")
        count += 1
    else:
        print(line, "Naughty")

#assert count == 2
#28 is too low, not 41, not 46, not 51
print(count)
