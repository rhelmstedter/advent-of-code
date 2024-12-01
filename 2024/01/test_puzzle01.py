from puzzle01 import part1, part2

SAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""


PART1_EXPECTED = 11
PART2_EXPECTED = 31


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED
