# import pytest

from puzzle import part1, part2

SAMPLE_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
EXAMPLE_LINES = [line.strip("\n") for line in SAMPLE_INPUT.split()]
PART1_EXPECTED = 157
PART2_EXPECTED = 70


def test_part1():
    actual = part1(EXAMPLE_LINES)
    assert actual == PART1_EXPECTED


def test_part2():
    actual = part2(EXAMPLE_LINES)
    assert actual == PART2_EXPECTED
