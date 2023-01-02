from dataclasses import dataclass
import re


@dataclass
class Point:
    x: int
    y: int

    def __str__(self):
        return f"{self.x},{self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def get_sensors_and_beacons():
    sensors = {}
    beacons = {}
    with open("./advent_of_code_2022/day15/input.txt") as fp:
        lines = fp.readlines()
        for l in lines:
            sensor_str, beacon_str = l.split(":")
            sensor_x, sensor_y = point_from_str(sensor_str)
            beacon_x, beacon_y = point_from_str(beacon_str)
            sensor_point = Point(int(sensor_x), int(sensor_y))
            beacon_point = Point(int(beacon_x), int(beacon_y))
            sensors[str(sensor_point)] = sensor_point
            beacons[str(beacon_point)] = beacon_point
    return sensors, beacons


def get_input():
    sensor_and_beacons = []
    with open("./advent_of_code_2022/day15/input.txt") as fp:
        lines = fp.readlines()
        for l in lines:
            sensor_str, beacon_str = l.split(":")
            sensor_x, sensor_y = point_from_str(sensor_str)
            beacon_x, beacon_y = point_from_str(beacon_str)
            sensor_point = Point(int(sensor_x), int(sensor_y))
            beacon_point = Point(int(beacon_x), int(beacon_y))
            # sensors[str(sensor_point)] = sensor_point
            # beacons[str(beacon_point)] = beacon_point
            sensor_and_beacons.append((sensor_point, beacon_point))
    return sensor_and_beacons


def point_from_str(s) -> tuple[int, int]:
    co_regex = r".*x=(?P<x>-*\d+).*y=(?P<y>-*\d+)"
    m = re.match(co_regex, s)

    if not m:
        raise ValueError(f"No match for string: {s}")
    # print(m.groupdict())
    return m.group("x"), m.group("y")


def get_bounds(points):
    max_x, min_x, max_y, min_y = 0, 0, 0, 0
    for p in points:
        if p.x > max_x:
            max_x = p.x
        if p.x < min_x:
            min_x = p.x
        if p.y > max_y:
            max_y = p.y
        if p.y < min_y:
            min_y = p.y
    return Point(min_x, min_y), Point(max_x, max_y)


def taxicab_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def impossible_position(pos: Point, sensors_and_beacons: list[tuple[Point, Point]]):
    for s, b in sensors_and_beacons:
        dist = taxicab_distance(s, b)
        if taxicab_distance(pos, s) <= dist and pos != b:
            return True
    return False


def points_in_distance(p: Point, d: int):
    points = []
    start_x = p.x - d
    end_x = p.x + d
    start_y = p.y - d
    end_y = p.y + d
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            ref = Point(x, y)
            if taxicab_distance(p, ref) < d:
                points.append(Point(x, y))
    return points


def part1():
    sensor_and_beacons = get_input()
    no_beacon_count = 0
    target_y = 2_000_000
    for x in range(-9000000, 9000000):
        if impossible_position(Point(x, target_y), sensor_and_beacons):
            no_beacon_count += 1
    print(no_beacon_count)
    return no_beacon_count


def part1_():
    sensor_and_beacons = get_input()
    no_beacons = set()
    beacons = set()
    for s, b in sensor_and_beacons:
        d = taxicab_distance(s, b)
        points = points_in_distance(s, d)
        no_beacons = no_beacons | set(points)
        beacons.add(b)
    no_beacons = no_beacons - beacons

    target_y = 10
    count = 0
    for p in no_beacons:
        if p.y == target_y:
            count += 1
    print(count)


def part1_too_slow():
    # sensors, beacons = get_sensors_and_beacons()
    # bounds = get_bounds(list(sensors.values()) + list(beacons.values()))
    sensor_and_beacons = get_input()
    no_beacons = set()
    beacons = set()
    for s, b in sensor_and_beacons:
        d = taxicab_distance(s, b)
        points = points_in_distance(s, d)
        no_beacons = no_beacons | set(points)
        beacons.add(b)
    no_beacons = no_beacons - beacons

    target_y = 10
    count = 0
    for p in no_beacons:
        if p.y == target_y:
            count += 1
    # print(count)

    # print(len(no_beacons))


# p = Point(2, 2)
# ans = points_in_distance(p, 2)
# print(ans)
# print(len(ans))


part1()
