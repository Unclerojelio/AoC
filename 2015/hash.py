import hashlib

def hash(secret, length):
    prefix = ""
    for _ in range(length):
        prefix += '0'
    for i in range(10000000):
        str2hash = secret + str(i)
        result = hashlib.md5(str2hash.encode())
        if result.hexdigest()[:length] == prefix:
            return i

secret = "yzbqklnj"
print(f"Part 1: {hash(secret, 5)} Part 2: {hash(secret, 6)}")