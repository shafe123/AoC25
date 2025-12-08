def read_file(
    input_file: str, strip: bool = True, split_str: bool = False
) -> list[str] | list[list[str]]:
    result = []
    with open(input_file) as in_file:
        for line in in_file:
            if strip:
                line = line.strip()
            if line and split_str:
                line = [char for char in line]

            result.append(line)

    return result


def get_lines(
    day: int, is_test: bool, strip: bool = True, split_str: bool = False
) -> list[str] | list[list[str]]:
    if is_test:
        file = f"data/day{day:02}_sample.txt"
    else:
        file = f"data/day{day:02}.txt"

    return read_file(file, strip, split_str)


def print_grid(grid: list[list], width=None):
    for row in grid:
        for val in row:
            if not width:
                print(val, end="")
            else:
                print(f"{str(val).rjust(width)}", end="")
        print()


def grid_string(grid: list[list]):
    return "".join(["".join(row) for row in grid])


def add_tuples[T](tuple_one: tuple[T, T], tuple_two: tuple[T, T]) -> tuple[T, T]:
    assert len(tuple_one) == 2 and len(tuple_two) == 2
    return tuple([one + two for one, two in zip(tuple_one, tuple_two)])  # type: ignore


def separator(name=None):
    def breaker(func):
        def inner(*args, **kwargs):
            if not name:
                split = getattr(func, "__name__", None)
            else:
                split = name
            print(f"------{split}-------")
            value = func(*args, **kwargs)
            print(f"------{split}-------")
            return value

        return inner

    return breaker
