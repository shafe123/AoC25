from utilities import *


@separator()
def part1(testing=True):
    data = get_lines(2, testing, True)
    segments = "".join(data).split(",")
    result = 0
    for segment in segments:
        lower, upper = segment.split("-")
        for num in range(int(lower), int(upper) + 1):
            str_num = str(num)

            # skip odd length numbers
            if len(str_num) % 2 == 1:
                continue

            if str_num[: len(str_num) // 2] == str_num[len(str_num) // 2 :]:
                result += num
    return result


@separator()
def part2(testing=True):
    data = get_lines(2, testing, True)
    segments = "".join(data).split(",")
    result = 0
    for segment in segments:
        lower, upper = segment.split("-")
        print(f"Analyzing {segment}")
        for num in range(int(lower), int(upper) + 1):
            str_num = str(num)

            for split_length in range(1, len(str_num) // 2 + 1):
                # print(f"Analyzing {str_num} for {str_num[:split_length]}...")
                # this split is not "complete"
                if len(str_num) / split_length != len(str_num) // split_length:
                    continue

                # count how many times the split occurs in the number
                if (
                    str_num.count(str_num[:split_length])
                    == len(str_num) // split_length
                ):
                    result += num
                    print(f"Found {str_num} for {str_num[:split_length]}!")
                    break

    return result


print(part2(False))
