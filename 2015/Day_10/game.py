input = "1113122113"

def solve(input):
    output = ""
    while len(input) > 0:
        i = 0
        c = input[i]
        count = 0
        while i < len(input):
            if c != input[i]:
                break
            count += 1
            i += 1
        input = input[i:]
        output += str(count) + c
    return output

for _ in range(40):
    output = solve(input)
    print(len(output))
    input = output
