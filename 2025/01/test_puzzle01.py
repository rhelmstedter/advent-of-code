from puzzle01 import part1, part2

SAMPLE_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


PART1_EXPECTED = 3
PART2_EXPECTED = 6


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED


if __name__ == "__main__":
    print(part2(SAMPLE_INPUT.splitlines()))
