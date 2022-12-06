from puzzle06 import part1, part2

SAMPLE_INPUT = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
EXAMPLE_LINES = [line.strip("\n") for line in SAMPLE_INPUT.split()]
PART1_EXPECTED = 7
PART2_EXPECTED = 19


def test_part1():
    actual = part1(SAMPLE_INPUT)
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT)
    assert actual == PART2_EXPECTED
