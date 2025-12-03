from utilities import *

@separator()
def part1(testing = True):
    data = get_lines(1, testing, True)

    current_pos = 50
    num_zeros = 0
    for line in data:
        direction, digits = line[0], int(line[1:])
        if direction == 'L':
            current_pos -= digits
        else:
            current_pos += digits
        
        while current_pos < 0:
            current_pos += 100
        while current_pos > 99:
            current_pos -= 100
        
        if (testing):
            print(current_pos)

        if current_pos == 0:
            num_zeros += 1

    return num_zeros

print(part1(False))