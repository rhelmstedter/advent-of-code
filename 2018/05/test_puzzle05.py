from puzzle05 import part1, part2

SAMPLE_INPUT = """dabAcCaCBAcCcaDA"""


PART1_EXPECTED = 10
PART2_EXPECTED = 4


def test_part1():
    actual = part1(SAMPLE_INPUT)
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT)
    assert actual == PART2_EXPECTED
