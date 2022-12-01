from advent_of_code_2022.day0 import day0


def test_fizz_buzz():
    test_n = 15
    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
    assert day0.fizz_buzz(test_n) == expected
