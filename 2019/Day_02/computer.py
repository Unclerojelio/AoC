f = open("input.txt", "r")
line = f.readlines()

ibytes = []
bytes = line[0].rstrip().split(',')
for byte in bytes:
    ibytes.append(int(byte))
# ibytes = [1,0,0,0,99] #[2, 0, 0, 0, 99]
# ibytes = [2,3,0,3,99] #[2, 3, 0, 6, 99]
# ibytes = [2,4,4,5,99,0] #[2, 4, 4, 5, 99, 9801]
# ibytes = [1,1,1,4,99,5,6,0,99] #[30, 1, 1, 4, 2, 5, 6, 0, 99]

ibytes[1] = 12
ibytes[2] = 2
for i in range(0, len(ibytes) - 1, 4):
    opcode = ibytes[i]
    if opcode == 99:
        break
    operand1 = ibytes[i+1]
    operand2 = ibytes[i+2]
    output = ibytes[i+3]
    print(f"opcode:\t{opcode}\toutput:\t{output}\toperand1:\t{operand1}\toperand2:\t{operand2}")
    if opcode == 1:
        ibytes[output] = ibytes[operand1] + ibytes[operand2]
    elif opcode == 2:
        ibytes[output] = ibytes[operand1] * ibytes[operand2]
print(ibytes[0])
