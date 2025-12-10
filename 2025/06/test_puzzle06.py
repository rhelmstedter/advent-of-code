from puzzle06 import part1, part2

SAMPLE_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


PART1_EXPECTED = 4277556
PART2_EXPECTED = 3263827


def test_part1():
    actual = part1(SAMPLE_INPUT.splitlines())
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(SAMPLE_INPUT.splitlines())
    assert actual == PART2_EXPECTED


if __name__ == "__main__":
    print(part2(SAMPLE_INPUT.splitlines()))
