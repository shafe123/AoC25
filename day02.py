from utilities import *


@separator()
def part1(testing=True):
    data = get_lines(2, testing, True)
    segments = ''.join(data).split(',')
    result = 0
    for segment in segments:
        lower, upper = segment.split('-')
        for num in range(int(lower), int(upper) + 1):
            str_num = str(num)
            
            # skip odd length numbers
            if len(str_num) % 2 == 1:
                continue

            if str_num[:len(str_num) // 2] == str_num[len(str_num) // 2 : ]:
                result += num
    return result

print(part1(False))