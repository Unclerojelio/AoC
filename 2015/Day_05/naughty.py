f = open("input.txt", "r")
#lines = f.readlines()
lines = [line.rstrip() for line in f.readlines()]

#lines = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']

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

nice_list = []
for line in lines:
    if not has_bad_words(line) and has_vowels(line) and has_doubles(line):
        nice_list.append(line)
        #print(line)
print(len(nice_list))