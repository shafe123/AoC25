from utilities import *


@separator()
def part1(testing=True):
    data = get_lines(1, testing, True)

    current_pos = 50
    num_zeros = 0
    for line in data:
        direction, digits = line[0], int(line[1:])
        if direction == "L":
            current_pos -= digits
        else:
            current_pos += digits

        while current_pos < 0:
            current_pos += 100
        while current_pos > 99:
            current_pos -= 100

        if testing:
            print(current_pos)

        if current_pos == 0:
            num_zeros += 1

    return num_zeros


@separator()
def part2(testing=True):
    data = get_lines(1, testing, True)

    position = 50
    zero_count = 0
    for line in data:
        direction = line[0]
        clicks = int(line[1:])

        # Move 1 click instead
        for _ in range(clicks):
            if direction == 'L':
                position = (position - 1) % 100
            else: # direction R
                position = (position + 1) % 100

            if position == 0:
                zero_count += 1
    return zero_count


# print(part1(False))
print(part2(False))
