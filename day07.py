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


if __name__ == "__main__":
    result = part1(False)
    print(result)
