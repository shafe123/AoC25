from utilities import *


@separator()
def part1(testing=True):
    data: list[list[str]] = get_lines(7, testing, split_str=True)  # type: ignore

    start_col = data[0].index("S")
    # use a set to keep track of which columns are there
    current_row_beams = {start_col}
    split_count = 0

    for row_num, row in enumerate(data):
        if row_num == 0:
            continue

        previous_row_beams = current_row_beams.copy()
        current_row_beams = set()

        for col_num, col in enumerate(row):
            # propagate the tachyon further down
            if col_num in previous_row_beams and col != "^":
                current_row_beams.add(col_num)

            # split the beam
            elif col_num in previous_row_beams and col == "^":
                current_row_beams.add(col_num - 1)
                current_row_beams.add(col_num + 1)
                split_count += 1

    return split_count


@separator()
def part2_att1(testing=True):
    data: list[list[str]] = get_lines(7, testing, split_str=True)  # type: ignore

    start_col = data[0].index("S")
    # use a LIST to keep track of which columns are there
    current_row_beams = [start_col]

    for row_num, row in enumerate(data):
        if row_num == 0:
            continue

        previous_row_beams = current_row_beams.copy()
        current_row_beams = []

        # go by beam instead of by column (which I should've done above)
        num_beams = len(previous_row_beams)
        beam_index = 0
        while beam_index < num_beams:
            # propagate the tachyon further down
            col_index = previous_row_beams[beam_index]
            if row[col_index] != "^":
                current_row_beams.append(col_index)
                # only increment here when we don't delete the beam
                beam_index += 1

            # split the beam (and remove the current beam)
            elif row[col_index] == "^":
                current_row_beams.append(col_index - 1)
                current_row_beams.append(col_index + 1)

                del previous_row_beams[beam_index]
                num_beams -= 1

    return current_row_beams


@separator()
def part2_att2(testing=True):
    data: list[list[str]] = get_lines(7, testing, split_str=True)  # type: ignore

    start_col = data[0].index("S")
    # use a dictionary to keep indices + counts
    current_row_beams = {start_col: 1}

    for row_num, row in enumerate(data):
        if row_num == 0:
            continue

        previous_row_beams = current_row_beams.copy()
        current_row_beams = dict()

        # go by beam instead of by column (which I should've done above)
        for col_index, count in previous_row_beams.items():
            # propagate the tachyon further down
            if row[col_index] != "^":
                if col_index in current_row_beams:
                    current_row_beams[col_index] += count
                else:
                    current_row_beams[col_index] = count

            # split the beam (and remove the current beam)
            elif row[col_index] == "^":
                # if the tachyon already exists in the dict, we need to add it the other one
                # left split
                if col_index - 1 in current_row_beams:
                    current_row_beams[col_index - 1] += count
                else:
                    current_row_beams[col_index - 1] = count

                # do the same for the right
                if col_index + 1 in current_row_beams:
                    current_row_beams[col_index + 1] += count
                else:
                    current_row_beams[col_index + 1] = count

        # debugging...
        if testing:
            width = 3
            for index, value in enumerate(row):
                if index in current_row_beams:
                    row[index] = current_row_beams[index]

                if isinstance(row[index], str):
                    print(row[index].rjust(width), end="")
                else:
                    print(f"{row[index]:{width}}", end="")
            print()

    return current_row_beams


if __name__ == "__main__":
    result = part2_att2(False)
    print(result)
    print(sum([count for count in result.values()]))
