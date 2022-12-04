from typing import Callable


def read_file() -> list[str]:
    with open(f"./advent_of_code_2022/day4/input.txt") as fp:
        return fp.readlines()


def part_1():
    result = count_range_events(full_overlap)
    return result


def part_2():
    result = count_range_events(any_overlap)
    return result


def count_range_events(count_event: Callable[[int, int, int, int], bool]):
    lines = read_file()
    lines = [l.strip() for l in lines]
    count = 0
    for l in lines:
        ranges = l.split(",")
        range_1 = ranges[0]
        range_2 = ranges[1]
        start_1, end_1 = range_1.split("-")
        start_2, end_2 = range_2.split("-")
        if count_event(int(start_1), int(end_1), int(start_2), int(end_2)):
            count += 1
    return count


def full_overlap(start_1: int, end_1: int, start_2: int, end_2: int) -> bool:
    if start_1 <= start_2 and end_1 >= end_2:
        return True
    if start_2 <= start_1 and end_2 >= end_1:
        return True
    return False


def any_overlap(start_1: int, end_1: int, start_2: int, end_2: int) -> bool:
    if start_1 <= start_2 <= end_1 or start_1 <= end_2 <= end_1:
        return True
    if start_2 <= start_1 <= end_2 or start_2 <= end_1 <= end_2:
        return True
    return False


print(part_1())
print(part_2())
