def read_file() -> list[str]:
    with open("./advent_of_code_2022/day2/input.txt") as fp:
        return fp.readlines()


shapePoints = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

draw = 3
win = 6

def score1(moves: str):
    match moves:
        case "A X":
            return shapePoints["X"] + draw
        case "A Y":
            return shapePoints["Y"] + win
        case "A Z":
            return shapePoints["Z"]
        case "B X":
            return shapePoints["X"]
        case "B Y":
            return shapePoints["Y"] + draw
        case "B Z":
            return shapePoints["Z"] + win
        case "C X":
            return shapePoints["X"] + win
        case "C Y":
            return shapePoints["Y"]
        case "C Z":
            return shapePoints["Z"] + draw

def score2(opponent: str, outcome: str):
    if opponent == "A":
        if outcome == "X":
            return shapePoints["Z"]
        if outcome == "Y":
            return shapePoints["X"] + draw
        if outcome == "Z":
            return shapePoints["Y"] + win
    if opponent == "B":
        if outcome == "X":
            return shapePoints["X"]
        if outcome == "Y":
            return shapePoints["Y"] + draw
        if outcome == "Z":
            return shapePoints["Z"] + win
    if opponent == "C":
        if outcome == "X":
            return shapePoints["Y"]
        if outcome == "Y":
            return shapePoints["Z"] + draw
        if outcome == "Z":
            return shapePoints["X"] + win


def part_1():
    lines = read_file()
    lines = [l.strip("\n") for l in lines]
    total_score = 0
    for l in lines:
        total_score += score1(l) 

def part_2():
    lines = read_file()
    lines = [l.strip("\n") for l in lines]
    total_score = 0
    for l in lines:
        opponent_move = l[0]
        outcome = l[2]
        total_score += score2(opponent_move, outcome) 
    return total_score
    



print(part_2())