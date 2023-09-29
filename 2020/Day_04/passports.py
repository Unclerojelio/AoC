f = open("2020/Day_04/input.txt", "r")
lines = f.readlines()

def process_lines(lines):
    concat_line = ''
    concat_lines = []
    for line in lines:
        line = line.rstrip()
        if len(line) > 0:
            concat_line += line + ' '
        else:
            concat_lines.append(concat_line)
            concat_line = ''
    concat_lines.append(concat_line)
    return concat_lines

def create_records(lines):
    records = []
    for line in lines:
        line = line.rstrip()
        record = line.split(' ')
        records.append(record)
    return records

def create_passports(records):
    passports = []
    passport = {}
    for record in records:
        for field in record:
            key, value = field.split(':')
            passport[key] = value
        passports.append(passport)
        passport = {}
    return passports

def validate_height(height):
    if height[-2:] == 'cm':
        if int(height[:-2]) < 150 or int(height[:-2]) > 193:
            return True
    elif height[-2:] == 'in':
        if int(height[:-2]) < 59 or int(height[:-2]) > 76:
            return True
    elif height[-2:] != 'cm' or height[-2:] != 'in':
        return True
    return False

def validate_hair_color(color):
    legal_chars = '0123456789abcdef'
    if color[:1] != "#" or len(color[1:]) != 6:
        return True
    for c in color[1:]:
        if c not in legal_chars:
            return True
    return False

def validate_eye_color(color):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not color in colors:
        return True
    return False

def validate_pid(pid):
    digits = '0123456789'
    if len(pid) != 9:
        return True
    for c in pid:
        if c not in digits:
            return True
    return False

def simple_validate(passports):
    count = 0
    for passport in passports:
        if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
            count += 1
    return count

def complex_validate(passports):
    count = 0
    for passport in passports:
        valid = True
        if not 'byr' in passport or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            valid = False
        if not 'iyr' in passport or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            valid = False
        if not 'eyr' in passport or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            valid = False
        if not 'hgt' in passport or validate_height(passport['hgt']):
            valid = False
        if not 'hcl' in passport or validate_hair_color(passport['hcl']):
            valid = False
        if not 'ecl' in passport or validate_eye_color(passport['ecl']):
            valid = False
        if not 'pid' in passport or validate_pid(passport['pid']):
            valid = False
        if valid:
            count += 1
    return count

passports = create_passports(create_records(process_lines(lines)))
print(f"Part 1: {simple_validate(passports)} Part 2: {complex_validate(passports)}")
