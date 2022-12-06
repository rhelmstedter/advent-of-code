from puzzle import part1, part2

SAMPLE_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
EXAMPLE_LINES = [line.strip("\n") for line in SAMPLE_INPUT.split()]
PART1_EXPECTED = 2
PART2_EXPECTED = 4


def test_part1():
    actual = part1(EXAMPLE_LINES)
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(EXAMPLE_LINES)
    assert actual == PART2_EXPECTED
