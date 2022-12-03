import os


def read_file():
    c = os.getcwd()
    print(c)
    with open(f"./advent_of_code_2022/day1/input.txt") as fp:
        return fp.readlines()


def part_1():
    lines = read_file()
    elves_total_calories = total_calories_per_elf(lines)
    # return elf with most total calories
    return max(elves_total_calories)


def part_2():
    lines = read_file()
    elves_total_calories = total_calories_per_elf(lines)
    # Sort elves by total calories in descending order
    total_calories_sorted = sorted(elves_total_calories, reverse=True)
    return (
        total_calories_sorted[0] + total_calories_sorted[1] + total_calories_sorted[2]
    )


def total_calories_per_elf(lines: list[str]):
    lines: list[str] = read_file()
    elf_rations: list[list[int]] = []
    current_elfs_rations: list[int] = []
    for line in lines:
        # Each elf's rations is separated by a single newline character
        if line == "\n":
            elf_rations.append(current_elfs_rations)
            current_elfs_rations = []
        else:
            # Each line of input has a trailing newline character
            line.strip("\n")
            current_elfs_rations.append(int(line))
    elves_total_calories: list[int] = []
    for e in elf_rations:
        elves_total_calories.append(sum(e))

    return elves_total_calories
