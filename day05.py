from utilities import *


def extract_ranges(ranges: list[list[int]]) -> list[list[int]]:
    final_ranges = [ranges[0]]
    for start_low, start_high in ranges[1:]:
        for index, (low, high) in enumerate(final_ranges):
            # keep going until if we're higher than this range
            if start_low > low and start_high > high:
                continue

            # simple insert if we're at the right place
            if start_low < low and start_high < high:
                final_ranges.insert(index + 1, [start_low, start_high])
                break

            # we're in the middle of this range, so no need to change the list
            if start_low >= low and start_high <= high:
                break

            # the low number is in the list but the high number is higher
            # need to update the higher end of this range
            if high >= start_low >= low and start_high > high:
                final_ranges[index][1] = start_high
                break

            # if the lower number is lower but the high number is in the range
            # need to update the beginning end of this range
            if start_low < low and low <= start_high <= high:
                final_ranges[index][0] = start_low
                break
        else:
            final_ranges.append([start_low, start_high])

        final_ranges = collapse_list(final_ranges)
    return final_ranges


def collapse_list(input_list: list[list[int]]) -> list[list[int]]:
    """
    Collapses a list of overlapping or adjacent ranges into a minimal set of non-overlapping ranges.
    Checks for multiple overlaps in series.
    Args:
        input_list (list of lists): A list of lists, where each tuple represents a range as [start, end].
    Returns:
        list of lists: A list of collapsed ranges as lists [start, end], with all overlaps and adjacencies merged.
    Example:
        collapse_list([[1, 5], [3, 7], [8, 10]]) -> [[1, 7], [8, 10]]

    >>> collapse_list([[1, 5], [3, 6], [8, 10]])
    [[1, 6], [8, 10]]
    >>> collapse_list([[1, 2], [3, 4], [5, 6]])
    [[1, 6]]
    >>> collapse_list([[1, 4], [2, 6], [5, 8]])
    [[1, 8]]
    >>> collapse_list([[1, 5], [2, 4]])
    [[1, 5]]
    >>> collapse_list([])
    []
    """
    new_list = sorted(input_list)
    index = 0
    while index < len(new_list) - 1:
        first_low, first_high = new_list[index]
        second_low, second_high = new_list[index + 1]

        # [1, 3], [2, 4] -> [1, 4]
        if (
            second_low <= first_high <= second_high
        ):  # these two ranges partially overlap
            # remove the second range and extend the first range
            new_list[index][1] = second_high
            new_list.pop(index + 1)

        # [1, 3], [4, 5] -> [1, 5]
        elif (
            first_high + 1 == second_low and first_high <= second_high
        ):  # these two ranges are just offset by 1
            # remove the second range and extend the first range
            new_list[index][1] = second_high
            new_list.pop(index + 1)

        # [1, 4], [2, 3] -> [1, 4]
        elif (
            first_low <= second_low and first_high >= second_high
        ):  # second range covered by first
            # remove the second range
            new_list.pop(index + 1)

        # look at the next item finally
        else:
            index += 1
    return new_list


def parse_lines(data: list[str], testing: bool) -> tuple[list[list[int]], list[int]]:
    ranges = []
    ids = []

    data_iter = iter(data)
    line = next(data_iter)
    while line != "":
        if testing:
            print(line)
        start, stop = line.split("-")
        ranges.append([int(start), int(stop)])
        line = next(data_iter)

    line = next(data_iter, "")
    while line != "":
        if testing:
            print(line)
        ids.append(int(line))
        line = next(data_iter, "")
    return ranges, ids


@separator()
def part1(testing=True):
    data = get_lines(5, testing)
    ranges, ids = parse_lines(data, testing)  # type: ignore

    fresh = []
    for id in ids:
        for low, high in ranges:
            if low <= id <= high:
                fresh.append(id)
                break
    return fresh


@separator()
def part2(testing=True):
    data = get_lines(5, testing)
    ranges, _ = parse_lines(data, testing)  # type: ignore

    final_ranges = extract_ranges(ranges)
    total_ids = 0
    for low, high in final_ranges:
        total_ids += high - low + 1

    return total_ids


if __name__ == "__main__":
    result = part2(False)
    print(result)
    # print(len(result))
