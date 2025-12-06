from utilities import *

from functools import reduce  # Required in Python 3
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


@separator()
def part1(testing=True):
    data: list[str] = get_lines(6, testing)  # type: ignore
    split_data = [row.split() for row in data]
    cols = []
    num_cols = len(split_data[0])
    for index, col in enumerate(range(num_cols)):
        new_col = []
        # convert all the integers
        for row in split_data[:-1]:
            new_col.append(int(row[col]))
        # append the operator
        new_col.append(split_data[-1][col])
        cols.append(new_col)

    values = []
    for col in cols:
        if col[-1] == "+":
            values.append(sum(col[:-1]))
        else:
            values.append(prod(col[:-1]))
    return values


@separator()
def part2(testing=True):
    data: list[str] = get_lines(6, testing, strip=False)  # type: ignore
    num_cols = len(data[0])
    num_rows = len(data)

    values = []
    numbers = []
    operator = sum  # just make the linter happy

    # column-wise ordering
    for col in range(num_cols):
        # print(col)
        if data[-1][col] in ["+", "*"]:  # start of a new set of numbers
            numbers = []
            operator = sum if data[-1][col] == "+" else prod

        this_number = []
        for row in range(num_rows - 1):
            this_number.append(data[row][col].strip())
        # are we in a blank columna and do we have numbers?
        if all([num == "" for num in this_number]) and numbers:
            # compute the value for the given math
            # print(numbers)
            values.append(operator(numbers))
        else:
            numbers.append(int("".join(this_number)))
    return values


if __name__ == "__main__":
    result = part2(False)
    print(result)
    print(sum(result))
