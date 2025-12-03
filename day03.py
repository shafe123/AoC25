from utilities import *


@separator()
def part1(testing=True):
    data = get_lines(3, testing, True)

    joltages = []
    for line in data:
        # get highest number from left
        left_max = -1
        left_index = -1

        # leave out the last number
        for count, x in enumerate(line[:-1]):
            if int(x) > left_max:
                left_max = int(x)
                left_index = count

        # get largest number after highest
        right_max = -1
        right_index = -1
        for count, x in enumerate(line[left_index + 1 :]):
            if int(x) > right_max:
                right_max = int(x)
                right_index = count + left_index + 1

        joltages.append(left_max * 10 + right_max)

    print(joltages)
    return sum(joltages)


@separator()
def part2(testing=True):
    num_vals = 12
    data = get_lines(3, testing, True)
    joltages = []

    for line in data:
        maxes = []
        indices = []
        print(line)
        while len(maxes) < num_vals:
            # get highest number from left
            max = -1
            index = -1

            # leave out the last N numbers
            beginning = indices[-1] + 1 if len(indices) else 0
            end = len(line) - (num_vals - len(indices)) + 1
            # print(f"Slicing from {beginning} to {end}")
            for count, x in enumerate(line[beginning:end]):
                if int(x) > max:
                    max = int(x)
                    index = count + beginning

            # print(f"Found: {max} at {index}")
            maxes.append(max)
            indices.append(index)

        joltages.append(int("".join([str(max) for max in maxes])))
        # joltages.append(left_max * 10 + right_max)

    print(joltages)
    return sum(joltages)


print(part2(False))
