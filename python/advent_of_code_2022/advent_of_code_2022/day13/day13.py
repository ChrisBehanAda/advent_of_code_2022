from functools import cmp_to_key


def get_pairs():
    pairs = []
    with open("./advent_of_code_2022/day13/input.txt") as fp:
        lines = fp.readlines()
        pair = []
        for l in lines:
            if l == "\n":
                pairs.append(pair)
                pair = []
            else:
                pair.append(eval(l.strip()))
        pairs.append(pair)
        return pairs


def get_packets():
    packets = []
    with open("./advent_of_code_2022/day13/input.txt") as fp:
        lines = fp.readlines()
        for l in lines:
            if l == "\n":
                pass
            else:
                packets.append(eval(l.strip()))
    return packets


def part1():
    pairs = get_pairs()
    pair_idx = 1
    out_of_order_indices = []
    while pair_idx <= len(pairs):
        l, r = pairs[pair_idx - 1][0], pairs[pair_idx - 1][1]
        if compare(l, r) == -1:
            out_of_order_indices.append(pair_idx)
        pair_idx += 1
    print(sum(out_of_order_indices))


def part2():
    divider_1 = [[2]]
    divider_2 = [[6]]
    packets = get_packets()
    packets += [divider_1, divider_2]
    sorted_packets = sorted(packets, key=cmp_to_key(compare))
    divider_1_idx = sorted_packets.index([[2]]) + 1
    divider_2_idx = sorted_packets.index([[6]]) + 1
    print(divider_1_idx * divider_2_idx)


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0

    if isinstance(l, list) and isinstance(r, list):
        idx = 0
        while idx < len(l) and idx < len(r):
            res = compare(l[idx], r[idx])
            if res != 0:
                return res
            idx += 1
        # Left list ran out of items first
        if len(l) < len(r):
            return -1
        # Right list ran out of items first
        if len(r) < len(l):
            return 1
    # Either left or right is not an int
    if type(l) != type(r):
        if isinstance(l, int):
            return compare([l], r)
        else:
            return compare(l, [r])
    # Empty list scenario
    return 0


# part1()
# part2()
