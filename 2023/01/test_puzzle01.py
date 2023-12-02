from puzzle01 import part1, part2

PART1_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


SAMPLE_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
PART1_EXPECTED = 142
PART2_EXPECTED = 281


def test_part1():
    actual = part1(PART1_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED
