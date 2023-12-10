from puzzle09 import part1, part2

SAMPLE_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


PART1_EXPECTED = 114
PART2_EXPECTED = 2


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED
