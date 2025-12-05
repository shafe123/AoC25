from utilities import *

def parse_lines(data, testing):
    ranges = []
    ids = []

    data_iter = iter(data)
    line = next(data_iter)
    while line != '':
        if testing: print(line)
        start, stop = line.split('-')
        ranges.append([int(start), int(stop)])
        line = next(data_iter)
    
    line = next(data_iter, '')
    while line != '':
        if testing: print(line)
        ids.append(int(line))
        line = next(data_iter, '')
    return ranges, ids

@separator()
def part1(testing=True):
    data = get_lines(5, testing)
    ranges, ids = parse_lines(data, testing)

    fresh = []
    for id in ids:
        for low, high in ranges:
            if low <= id <= high:
                fresh.append(id)
                break
    return fresh


    

if __name__ == "__main__":
    result = part1(False)
    print(result)
    print(len(result))