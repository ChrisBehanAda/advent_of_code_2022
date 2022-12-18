from dataclasses import dataclass
from enum import Enum
from typing import Optional


class InstructionType(Enum):
    NOOP = 1
    ADDR = 2


@dataclass
class Instruction:
    type_: InstructionType
    value: Optional[int] = 0


def get_input() -> list[str]:
    with open(f"./advent_of_code_2022/day10/input.txt") as fp:
        return fp.readlines()


def part_1():
    input_lines = get_input()
    instructions = get_instructions(input_lines)
    cycle = 1
    instruction_pointer = 0
    X = 1
    mid_cycle = False
    signal_strength_sums = 0
    while instruction_pointer < len(instructions):
        if (
            cycle == 20
            or cycle == 60
            or cycle == 100
            or cycle == 140
            or cycle == 180
            or cycle == 220
        ):
            signal_strength_sums += cycle * X
        current_instruction = instructions[instruction_pointer]
        if current_instruction.type_ == InstructionType.NOOP:
            instruction_pointer += 1
            mid_cycle = False
        else:
            if mid_cycle:
                X += current_instruction.value
                instruction_pointer += 1
                mid_cycle = False
            else:
                mid_cycle = True

        cycle += 1
    return signal_strength_sums


def part_2():
    screen = [["" for _ in range(40)] for _ in range(6)]
    sprite_pos = [0, 1, 2]

    input_lines = get_input()
    instructions = get_instructions(input_lines)
    cycle = 1
    instruction_pointer = 0
    X = 1
    mid_cycle = False
    while instruction_pointer < len(instructions):
        row = (cycle - 1) // 40
        col = (cycle - 1) % 40
        draw_pixel(screen=screen, sprite_pos=sprite_pos, col=col, row=row)

        current_instruction = instructions[instruction_pointer]
        if current_instruction.type_ == InstructionType.NOOP:
            instruction_pointer += 1
            mid_cycle = False
        else:
            if mid_cycle:
                X += current_instruction.value
                sprite_pos = sprite_position(X)
                instruction_pointer += 1
                mid_cycle = False
            else:
                mid_cycle = True

        cycle += 1
    print_screen(screen)


def draw_pixel(screen, sprite_pos, col, row):
    if col in sprite_pos:
        screen[row][col] = "#"
    else:
        screen[row][col] = "."


def sprite_position(center):
    return [center - 1, center, center + 1]


def print_screen(screen):
    for row in screen:
        print(row)


def get_instructions(lines: list[str]) -> list[Instruction]:
    instructions = []
    for l in lines:
        parts = l.split(" ")
        is_addr = len(parts) == 2
        if is_addr:
            i = Instruction(InstructionType.ADDR, int(parts[1]))
        else:
            i = Instruction(InstructionType.NOOP)
        instructions.append(i)
    return instructions
