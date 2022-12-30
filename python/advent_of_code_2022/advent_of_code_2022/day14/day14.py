import functools


class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"p1: ({self.x1},{self.y1}) p2: ({self.x2},{self.y2})"

    def is_vertical(self) -> bool:
        if self.x1 == self.x2:
            return True
        return False


def get_lines():
    line_list = []
    with open("./advent_of_code_2022/day14/input.txt") as fp:
        lines = fp.readlines()
        for l in lines:
            coordinates = []
            coordinate_strs = l.split("->")
            for co_str in coordinate_strs:
                co = co_str.strip()
                x_str, y_str = co.split(",")
                x, y = int(x_str), int(y_str)
                coordinates.append((x, y))
            line_list.extend(coordinates_to_lines(coordinates))
    return line_list


def coordinates_to_lines(coordinates):
    lines = []
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i][0], coordinates[i][1]
        x2, y2 = coordinates[i + 1][0], coordinates[i + 1][1]
        l = Line(x1, y1, x2, y2)
        lines.append(l)
    return lines


def create_grid(lines):
    max_x = functools.reduce(lambda x, l: max(x, l.x1, l.x2), lines, -1)
    max_y = functools.reduce(lambda y, l: max(y, l.y1, l.y2), lines, -1)
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    return grid


def create_big_grid_with_floor(lines, multiplier):
    max_x = functools.reduce(lambda x, l: max(x, l.x1, l.x2), lines, -1)
    max_y = functools.reduce(lambda y, l: max(y, l.y1, l.y2), lines, -1)
    max_x_multiplied = max_x * multiplier
    max_y_multiplied = max_y * multiplier
    grid = [
        ["." for _ in range(max_x_multiplied + 1)] for _ in range(max_y_multiplied + 1)
    ]
    for x in range(max_x_multiplied):
        grid[max_y + 2][x] = "#"
    return grid


def draw_lines(grid, lines):
    for l in lines:
        if l.is_vertical():
            for y in range(min(l.y1, l.y2), max(l.y1, l.y2) + 1):
                grid[y][l.x1] = "#"
        else:
            for x in range(min(l.x1, l.x2), max(l.x1, l.x2) + 1):
                grid[l.y1][x] = "#"


def can_drop(x, y, grid):
    if y >= len(grid) or x >= len(grid[0]):
        return False
    if grid[y][x] == ".":
        return True
    return False


def abyss(x, y, grid):
    if y >= len(grid):
        return True


def drop_sand(x, y, grid):
    if y >= len(grid) or x >= len(grid[0]):
        return False
    if abyss(x, y + 1, grid):
        return False
    if can_drop(x, y + 1, grid):
        return drop_sand(x, y + 1, grid)
    elif can_drop(x - 1, y + 1, grid):
        return drop_sand(x - 1, y + 1, grid)
    elif can_drop(x + 1, y + 1, grid):
        return drop_sand(x + 1, y + 1, grid)
    else:
        if grid[y][x] == "o":
            return False
        grid[y][x] = "o"
        return True


def drop_sand2(x, y, grid):
    if y >= len(grid) or x >= len(grid[0]):
        return False
    if can_drop(x, y + 1, grid):
        return drop_sand(x, y + 1, grid)
    elif can_drop(x - 1, y + 1, grid):
        return drop_sand(x - 1, y + 1, grid)
    elif can_drop(x + 1, y + 1, grid):
        return drop_sand(x + 1, y + 1, grid)
    else:
        if grid[y][x] == "o":
            return False
        grid[y][x] = "o"
        return True


def part1():
    lines = get_lines()
    grid = create_grid(lines)
    draw_lines(grid, lines)
    droppable = True
    count = 0
    while droppable:
        droppable = drop_sand(500, 0, grid)
        if droppable:
            count += 1
    # print(count)


def part2():
    lines = get_lines()
    grid = create_big_grid_with_floor(lines, 2)
    draw_lines(grid, lines)
    droppable = True
    count = 0
    while droppable:
        droppable = drop_sand2(500, 0, grid)
        if droppable:
            count += 1
    print(count)


# part1()
part2()
# print(create_grid(get_lines()))
