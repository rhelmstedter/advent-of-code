from functools import reduce
from typing import Tuple

def get_two_numbers_sum(expenses, expected) -> Tuple[int, int]:
    for i, first_value in enumerate(expenses):
        for j, second_value in enumerate(expenses):
            if i == j:
                continue
            if first_value + second_value == expected:
                break
    return first_value, second_value

def get_three_numbers_sum_to(expenses, expected) -> Tuple[int, int, int]:
    for i, first in enumerate(expenses):
        for j, second in enumerate(expenses):
            for k, third in enumerate(expenses):
                if i == j == k:
                    continue
                if first + second + third == expected:
                    break
    return first, second, third


def part_1():
    with open("inputs/day_1_input.txt", "r") as report:
        expenses = [int(expense.strip()) for expense in report.readlines()]

    values = get_two_numbers_sum(expenses, 2020)
    print(reduce(lambda x, y: x*y, values))

def part_2():
    with open("inputs/day_1_input.txt", "r") as report:
        expenses = [int(expense.strip('\n')) for expense in report.readlines()]

    values = get_three_numbers_sum_to(expenses=expenses, expected=2020)
    print(reduce(lambda x, y : x * y, values))


if __name__ == "__main__":
    part_1()
    part_2()
