from utilities import *


def count_adjacent(row: int, col: int, matrix: list[str], target: str = "@"):
    count = 0
    for y_offset in range(-1, 2):
        if row + y_offset < 0 or row + y_offset >= len(matrix):
            continue
        for x_offset in range(-1, 2):
            if (
                col + x_offset < 0
                or col + x_offset >= len(matrix[0])
                or (y_offset == 0 and x_offset == 0)
            ):
                continue
            if matrix[row + y_offset][col + x_offset] == target:
                count += 1
    return count


@separator()
def part1(testing=True):
    data = get_lines(4, testing, True)
    rows = len(data)
    cols = len(data[0])
    accessible = []
    for row in range(rows):
        for col in range(cols):
            if data[row][col] != "@":
                print(".", end="")
                continue

            adjacent_at = count_adjacent(row, col, data)
            print(adjacent_at, end="")
            if adjacent_at < 4:
                accessible.append((row, col))
        print()
    return accessible


@separator()
def part2(testing=True):
    data = get_lines(4, testing, True, True)
    rows = len(data)
    cols = len(data[0])
    accessible = [1, 2]
    total_removed = 0
    while len(accessible) > 0:
        accessible = []
        for row in range(rows):
            for col in range(cols):
                if data[row][col] != "@":
                    # print(".", end="")
                    continue

                adjacent_at = count_adjacent(row, col, data)
                # print(adjacent_at, end="")
                if adjacent_at < 4:
                    accessible.append((row, col))
            # print()
        print(accessible)
        for row, col in accessible:
            data[row][col] = "."
            total_removed += 1

    return total_removed


if __name__ == "__main__":
    result = part2(False)
    print(result)
