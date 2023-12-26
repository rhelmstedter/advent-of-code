from puzzle10 import part1, part2

SIMPLE_LOOP = """.....
.S-7.
.|.|.
.L-J.
.....
"""

COMPLEX_LOOP = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

PART1_SIMPLE = 4
PART1_COMPLEX = 8
PART2_EXPECTED = ...


def test_part1_simple():
    actual = part1(SIMPLE_LOOP.splitlines())
    assert actual == PART1_SIMPLE


def test_part1_complex():
    actual = part1(COMPLEX_LOOP.splitlines())
    assert actual == PART1_COMPLEX


# def test_part2():
#     actual = part2(SIMPLE_LOOP.splitlines())
#     assert actual == PART2_EXPECTED
