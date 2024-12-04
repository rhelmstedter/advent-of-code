from puzzle03 import part1, part2

SAMPLE_INPUT = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
SAMPLE_INPUT2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


PART1_EXPECTED = 161
PART2_EXPECTED = 48


def test_part1():
    actual = part1(SAMPLE_INPUT)
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT2)
    assert actual == PART2_EXPECTED
