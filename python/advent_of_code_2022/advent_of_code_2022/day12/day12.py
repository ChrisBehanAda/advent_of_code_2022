from queue import Queue


def get_input():
    grid = []
    with open("./advent_of_code_2022/day12/input.txt") as fp:
        lines = fp.readlines()
        for l in lines:
            row = []
            l = l.strip()
            for c in l:
                row.append(c)
            grid.append(row)
    return grid


def part1():
    grid = get_input()
    start_row, start_col = find_pos(grid, "S")
    end_row, end_col = find_pos(grid, "E")
    grid[start_row][start_col] = "a"
    grid[end_row][end_col] = "z"
    distances = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
    ans = bfs(grid, distances, start_row, start_col, end_row, end_col)
    return ans


def part2():
    grid = get_input()
    end_row, end_col = find_pos(grid, "E")
    start_row, start_col = find_pos(grid, "S")
    grid[start_row][start_col] = "a"
    grid[end_row][end_col] = "z"
    starting_positions = find_all_pos(grid, "a")
    min_steps = float("inf")
    for s_row, s_col in starting_positions:
        distances = [
            [float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))
        ]
        ans = bfs(grid, distances, s_row, s_col, end_row, end_col)
        if ans < min_steps:
            min_steps = ans

    return min_steps


def bfs(grid, distances, start_row, start_col, end_row, end_col):
    distances[start_row][start_col] = 0
    q = Queue()
    q.put((start_row, start_col))
    while not q.empty():
        r, c = q.get()
        adjacent_positions = adjacent(grid, r, c)
        for adj_row, adj_col in adjacent_positions:
            if distances[adj_row][adj_col] == float("inf"):
                distances[adj_row][adj_col] = distances[r][c] + 1
                q.put((adj_row, adj_col))
    return distances[end_row][end_col]


def find_pos(grid, target):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                return (r, c)
    return -1, -1


def find_all_pos(grid, target):
    all_positions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                all_positions.append((r, c))
    return all_positions


def adjacent(grid, row, col):
    # Ascii value of current grid position
    current_height = ord(grid[row][col])
    adjacent_positions = [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1),
    ]
    reachable_positions = []
    for r, c in adjacent_positions:
        if (
            0 <= r < len(grid)
            and 0 <= c < len(grid[0])
            and ord(grid[r][c]) <= current_height + 1
        ):
            reachable_positions.append((r, c))
    return reachable_positions
