f = open("input.txt", "r")
line = f.readlines()

ibytes = []
bytes = line[0].rstrip().split(',')
for byte in bytes:
    ibytes.append(int(byte))
    
for i in range(1000000):
    ibytes.append(0)

program = ibytes.copy()
for noun in range(100):
    for verb in range(100):
        ibytes = program.copy()
        ibytes[1] = noun
        ibytes[2] = verb
        for i in range(0, len(ibytes) - 1, 4):
            opcode = ibytes[i]
            if opcode == 99:
                break
            operand1 = ibytes[i+1]
            operand2 = ibytes[i+2]
            output = ibytes[i+3]
            if opcode == 1:
                ibytes[output] = ibytes[operand1] + ibytes[operand2]
            elif opcode == 2:
                ibytes[output] = ibytes[operand1] * ibytes[operand2]
        if ibytes[0] == 19690720:
            print(f"Final result:\t{100 * noun + verb}")
            exit()
