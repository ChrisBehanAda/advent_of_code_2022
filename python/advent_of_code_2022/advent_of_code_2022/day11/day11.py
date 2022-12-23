import functools


def get_input() -> list[str]:
    with open("./advent_of_code_2022/day11/input.txt") as fp:
        return fp.readlines()


def parse_monkey_lines(lines: list[str]):
    monkey_lines = []
    monkey = []
    for l in lines:
        if l == "\n":
            monkey_lines.append(monkey)
            monkey = []
        else:
            monkey.append(l.strip())
    monkey_lines.append(monkey)
    return monkey_lines


class Monkey:
    def __init__(
        self,
        id,
        items,
        operation,
        op_value,
        divisor,
        true_target,
        false_target,
    ):
        self.id = id
        self.items = items
        self.op = operation
        self.op_value = op_value
        self.divisor = divisor
        self.true_target = true_target
        self.false_target = false_target
        self.worry_level_divisor = 3
        self.inspection_count = 0

    @classmethod
    def from_lines(cls, lines):
        id_pos = len(lines[0]) - 2
        id = lines[0][id_pos]
        _, items_str = lines[1].split(":")
        items = items_str.split(",")
        items = [int(i) for i in items]
        op = "+" if "+" in lines[2] else "*"
        op_value_str = lines[2].split()[-1]
        op_value = int(op_value_str) if op_value_str.isnumeric() else "old"
        divisor_words = lines[3].split()
        divisor = [int(d) for d in divisor_words if d.isnumeric()][0]
        true_target_words = lines[4].split()
        true_target = [int(d) for d in true_target_words if d.isnumeric()][0]
        false_target_words = lines[5].split()
        false_target = [int(d) for d in false_target_words if d.isnumeric()][0]
        return cls(id, items, op, op_value, divisor, true_target, false_target)

    def throw(self, target):
        return self.items.pop(0)

    def catch(self, item):
        self.items.append(item)

    def operation(self, item, val):
        if self.op == "+":
            return item + val
        elif self.op == "*":
            return item * val
        else:
            raise ValueError(f"Unexpected operation: {self.op}")

    def test(self, worry_level):
        return worry_level % self.divisor == 0

    def inspect_and_throw(self):
        item = self.items.pop(0)
        value = item if self.op_value == "old" else self.op_value
        worry_level = self.operation(item, value)
        worry_level = worry_level // self.worry_level_divisor
        if self.test(worry_level):
            target = self.true_target
        else:
            target = self.false_target
        self.inspection_count += 1
        return worry_level, target

    def inspect_and_throw2(self, divisor_product):
        item = self.items.pop(0)
        value = item if self.op_value == "old" else self.op_value
        item = item % divisor_product
        worry_level = self.operation(item, value)
        if self.test(worry_level):
            target = self.true_target
        else:
            target = self.false_target
        self.inspection_count += 1
        return worry_level, target


def part1():
    lines = get_input()
    monkey_lines = parse_monkey_lines(lines)
    monkeys = []
    for m in monkey_lines:
        monkey = Monkey.from_lines(m)
        monkeys.append(monkey)

    # simulate_turns(20, monkeys)
    for _ in range(20):
        for m in monkeys:
            monkey_turn(m, monkeys)

    monkeys.sort(key=lambda m: m.inspection_count, reverse=True)
    return monkeys[0].inspection_count * monkeys[1].inspection_count


def part2():
    lines = get_input()
    monkey_lines = parse_monkey_lines(lines)
    monkeys = []
    for m in monkey_lines:
        monkey = Monkey.from_lines(m)
        monkey.worry_level_divisor = 1
        monkeys.append(monkey)

    for _ in range(10000):
        for m in monkeys:
            monkey_turn2(m, monkeys)

    for m in monkeys:
        print(m.__dict__)

    monkeys.sort(key=lambda m: m.inspection_count, reverse=True)
    return monkeys[0].inspection_count * monkeys[1].inspection_count


def simulate_turns(rounds, monkeys):
    for _ in range(rounds):
        for m in monkeys:
            monkey_turn(m, monkeys)


def monkey_turn(m: Monkey, monkeys: list[Monkey]):
    while len(m.items) > 0:
        worry_level, target = m.inspect_and_throw()
        monkeys[target].catch(worry_level)


def monkey_turn2(m: Monkey, monkeys: list[Monkey]):
    monkey_divisors = [m.divisor for m in monkeys]
    divisor_product = functools.reduce(lambda a, b: a * b, monkey_divisors)
    while len(m.items) > 0:
        worry_level, target = m.inspect_and_throw2(divisor_product)
        monkeys[target].catch(worry_level)


print(part2())
