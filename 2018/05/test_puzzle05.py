from puzzle05 import part1, part2
from puzzle05 import solve_part1, solve_part2

SAMPLE_INPUT = """dabAcCaCBAcCcaDA"""
with open("input.txt") as f:
    data = f.read().strip()

PART1_EXPECTED = 10
PART2_EXPECTED = 4


def test_part1():
    actual = part1(SAMPLE_INPUT)
    real = part1(data)
    assert real == 9348
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT)
    real = part2(data)
    assert actual == PART2_EXPECTED
    assert real == 4996
