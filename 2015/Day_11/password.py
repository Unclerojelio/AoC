import time
import string

def inc_pass(input):
    letters = string.ascii_lowercase
    i = len(input) - 1

    if input[i] == 'z':
        while input[i] == 'z':
            input = input[:i] + 'a' + input[i+1:] 
            i -= 1
        index = letters.index(input[i])
        input = input[:i] + letters[index + 1] + input[i+1:]
    else:
        index = letters.index(input[-1])
        input = input[:-1] + letters[index + 1]
    return input

def rule_1(input):
    triples = ['abc', 'bcd', 'cde','def','efg', 'fgh', 'ghi','hij','ijk','jkl','klm','lmn','mno','nop','opq', 'pqr', 'qrs','rst','stu','tuv','uvw','vwx','wxy','xyz']
    for triple in triples:
        if triple in input:
            return True
    return False

def rule_2(input):
    if 'i' in input or 'o' in input or 'l' in input:
        return False
    return True

def rule_3(input):
    doubles = ['aa', 'bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy', 'zz']
    finds = {}
    for double in doubles:
        index = input.find(double)
        if index != -1:
            finds[double] = index
    if len(finds) >= 2:
        return True
    return False

def solve(input):
    while True:
        input = inc_pass(input)
        if rule_2(input) and rule_1(input) and rule_3(input):
            return input

def main():
    start = time.time()
    input = "cqjxjnds"

    ans1 = solve(input)
    ans2 = solve(ans1)
    assert ans1 == 'cqjxxyzz'
    assert ans2 == 'cqkaabcc'
    print("Answer 1:", ans1, "Answer 2: ", ans2)

    end = time.time()
    print("Elapsed time:", (end-start) * 10**3, "ms")


if __name__=="__main__":
    main()
