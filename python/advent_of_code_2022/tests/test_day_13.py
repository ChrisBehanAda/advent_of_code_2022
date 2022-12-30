from advent_of_code_2022.day13 import day13


def test_part_1():
    # day13.part1()
    # a = "1,1,3,1,1"
    # ans = []
    day13.part1()
    # h, t = day13.string_list_to_list(a[0], a[1:], ans)
    # print(h)


def test_out_of_order():
    day13.out_of_order([1], [1, 2])


def test_in_order():
    day13.in_order([[1], [2, 3, 4]], [[1], 4])
