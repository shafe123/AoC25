from utilities import *
from math import sqrt

MAX_LENGTH = 1000


class Point:
    def __init__(self, coords: tuple[int, int, int]) -> None:
        self.x, self.y, self.z = coords

    def __sub__(self, value) -> float:
        if not isinstance(value, Point):
            raise TypeError
        return sqrt(
            (self.x - value.x) ** 2 + (self.y - value.y) ** 2 + (self.z - value.z) ** 2
        )

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Point):
            raise TypeError
        return self.x == value.x and self.y == value.y and self.z == value.z

    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Point):
            raise TypeError
        if self.x == value.x and self.y == value.y:
            return self.z < value.z
        elif self.x == value.x:
            return self.y < value.y

        return self.x < value.x

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def distance(cls, first, second):
        return first - second


@separator()
def part1(testing=True):
    data: list[str] = get_lines(8, testing)  # type: ignore

    points = []
    for line in data:
        x, y, z = line.split(",")
        points.append(Point((int(x), int(y), int(z))))

    points.sort()
    distance_map = generate_distance_map(points)
    distances = generate_sorted_distances(points, distance_map)
    circuits = generate_circuits(distances)
    circuits.sort(key=len, reverse=True)

    return circuits


@separator()
def generate_sorted_distances(points, distance_map):
    # here only do the upper triangle so we don't have duplicates
    distances = []
    for row in range(0, len(distance_map)):
        for col in range(row + 1, len(distance_map)):
            distances.append((distance_map[row][col], points[row], points[col]))
    distances.sort()
    # [print(elem) for elem in distances]
    return distances


@separator()
def generate_circuits(distances):
    circuits = []
    for distance, point_one, point_two in distances[:MAX_LENGTH]:
        circuit = None
        # see if it's in a circuit or not
        for index, circuit_list in enumerate(circuits):
            # do nothing here
            # fmt: off
            if ((point_one, point_two) in circuit_list 
                or (point_two, point_one) in circuit_list):
                break
            # fmt: on
            from_points = [pair[0] for pair in circuit_list]
            to_points = [pair[1] for pair in circuit_list]

            if point_one in from_points or point_one in to_points:
                circuit = index
                break
            elif point_two in from_points or point_two in to_points:
                circuit = index
                break
        else:
            circuits.append([])
            circuit = -1

        if circuit:
            circuits[circuit].append((point_one, point_two))
        # print(circuits)

    [print(circuit) for circuit in circuits]
    return circuits


@separator()
def generate_distance_map(points):
    distance_map = [[0 for _ in range(len(points))] for _ in range(len(points))]

    # only need the upper triangle, but doing the full matrix makes it easier (we can sort to find shortest distance)
    for row, point_one in enumerate(points):
        for col, point_two in enumerate(points):
            if point_one is point_two:
                continue

            distance_map[row][col] = point_one - point_two

    # print_grid(distance_map, 8)
    return distance_map


if __name__ == "__main__":
    result = part1(False)
    [print(circuit) for circuit in result[:3]]
    print(prod([len(circuit) + 1 for circuit in result[:3]]))
