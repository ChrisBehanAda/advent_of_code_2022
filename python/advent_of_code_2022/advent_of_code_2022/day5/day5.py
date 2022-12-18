from collections import defaultdict
from dataclasses import dataclass

import re
def get_input() -> list[str]:
    with open(f"./advent_of_code_2022/day5/input.txt") as fp:
        return fp.readlines()

def get_crate_lines(lines: list[str]) -> list[str]:
    reached_crate_label = False
    crate_lines = []
    for l in lines:
        if "1" in l:
            reached_crate_label = True
        if reached_crate_label:
            crate_lines.append(l)
            break
        else:
            crate_lines.append(l)
    return crate_lines

def get_crate_positions(label_line: str):
    # Map crate ids to their position in the input string
    crate_positions = {}
    for key, val in enumerate(label_line):
        if val.isnumeric():
            crate_positions[int(val)] = key
    return crate_positions

def build_crates(crate_lines: list[str], crate_positions: dict[int, int]) -> defaultdict[int, list[str]]:
    crates = defaultdict(list)
    # Iterate through create_lines from top to bottom
    for l in crate_lines[::-1]:
        for crate_pos, idx in crate_positions.items():
            if l[idx].isalpha():
                crates[crate_pos].append(l[idx])
    return crates

@dataclass
class Move:
    quantity: int
    from_pos: int
    to_pos: int

def parse_moves(lines: list[str]) -> list[Move]:
    move_regex = "move (\d+) from (\d+) to (\d+)"
    moves = []
    for l in lines:
        m = re.match(move_regex, l)
        if m:
            move = Move(quantity=int(m.group(1)), from_pos=int(m.group(2)), to_pos=int(m.group(3)))
            moves.append(move)
        else:
            raise ValueError(f"Move string '{l}' is invalid.")
    return moves


def get_move_lines(lines: list[str]) -> list[str]:
    move_lines = []
    for l in lines:
        if l.startswith("move"):
            move_lines.append(l)
    return move_lines

def make_move_9000(move: Move, crates):
    picked_up = crates[move.from_pos][-move.quantity:]
    # remove picked up crates
    crates[move.from_pos] = crates[move.from_pos][:-move.quantity]
    # append picked up crates to their destination
    while picked_up:
        top = picked_up.pop()
        crates[move.to_pos].append(top)

def make_move_9001(move: Move, crates):
    picked_up = crates[move.from_pos][-move.quantity:]
    # remove picked up crates
    crates[move.from_pos] = crates[move.from_pos][:-move.quantity]
    # append picked up crates to their destination
    crates[move.to_pos].extend(picked_up)

def top_of_crates(crates):
    msg = ""
    for _, c in crates.items():
        msg += c[-1]
    return msg

def move_crates(make_move):
    lines = get_input()
    crate_lines = get_crate_lines(lines)
    label_line = crate_lines.pop()
    crate_positions = get_crate_positions(label_line) 
    crates = build_crates(crate_lines, crate_positions)
    move_lines = get_move_lines(lines)
    moves = parse_moves(move_lines)
    for m in moves:
        make_move(m, crates)
    top_msg = top_of_crates(crates)
    return top_msg

def part_1():
    return move_crates(make_move_9000)

def part_2():
    return move_crates(make_move_9001)

print(part_1())
print(part_2())
