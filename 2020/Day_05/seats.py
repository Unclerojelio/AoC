import sys

lines = sys.stdin.readlines()
#lines = ['FBFBBFFRLR']
seat_ids = []

def find_seat(seat_ids):
    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids:
            return i

for line in lines:
    line = line.strip()
    row_front = 0
    row_back = 127
    for i in range(7):
        if line[i] == 'F':
            row_back = (row_back - row_front) // 2 + row_front
        else:
            row_front = (row_back - row_front) // 2 + row_front + 1

    column_left = 0
    column_right = 7
    for i in range(7, len(line)):
        if line[i] == 'L':
            column_right = (column_right - column_left) // 2 + column_left
        else:
            column_left = (column_right - column_left) // 2 + column_left + 1

    seat_ids.append(row_front * 8 + column_left)

print(f"Part 1: {max(seat_ids)} Part 2: {find_seat(sorted(seat_ids))}")