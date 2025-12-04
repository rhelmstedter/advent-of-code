from puzzle03 import part1, part2, get_data

SAMPLE_INPUT = """987654321111111
811111111111119
234234234234278
818181911112111
"""


PART1_EXPECTED = 357
PART2_EXPECTED = 3121910778619


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED
    assert part1(get_data(3)) == 17263


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED


if __name__ == "__main__":
    print(part2(SAMPLE_INPUT.splitlines()))
