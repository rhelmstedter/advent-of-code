from puzzle06 import part1, part2

SAMPLE_INPUT = """Time:      7  15   30
Distance:  9  40  200
"""


PART1_EXPECTED = 288
PART2_EXPECTED = 71503


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED
