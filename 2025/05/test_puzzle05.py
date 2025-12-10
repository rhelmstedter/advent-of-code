from puzzle05 import part1, part2

SAMPLE_INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


PART1_EXPECTED = 3
PART2_EXPECTED = 14


def test_part1():
    actual = part1(SAMPLE_INPUT)
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT)
    assert actual == PART2_EXPECTED

