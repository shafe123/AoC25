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


if __name__ == "__main__":
    result = part1(False)
    print(result)
    print(sum(result))
