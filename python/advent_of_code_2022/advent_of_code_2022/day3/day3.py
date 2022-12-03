def item_priority(item: str):
    if ord("a") <= ord(item) <= ord("z"):
        return ord(item) - ord("a") + 1
    elif ord("A") <= ord(item) <= ord("Z"):
        return ord(item) - ord("A") + 27
    else:
        raise ValueError(f"Invalid item: {item}")


def read_file() -> list[str]:
    with open("./advent_of_code_2022/day3/input.txt") as fp:
        return fp.readlines()


def part1():
    rucksacks = read_file()
    rucksacks = [r.strip() for r in rucksacks]
    priority_sum = 0
    for r in rucksacks:
        compartment_1 = r[: len(r) // 2]
        compartment_2 = r[len(r) // 2 :]
        items_1 = set(compartment_1)
        items_2 = set(compartment_2)
        common_items = items_1 & items_2
        common = common_items.pop()
        priority_sum += item_priority(common)

    return priority_sum

def part2():
    rucksacks = read_file()
    rucksacks = [r.strip() for r in rucksacks]
    badge_sum = 0
    for i in range(2, len(rucksacks), 3):
        items_1 = set(rucksacks[i-2])
        items_2 = set(rucksacks[i-1])
        items_3 = set(rucksacks[i])
        badge = (items_1 & items_2 & items_3).pop()
        badge_sum += item_priority(badge)
    return badge_sum


print(part1())
print(part2())