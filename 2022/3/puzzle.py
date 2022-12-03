from string import ascii_lowercase, ascii_uppercase

day = 3
PRIORITIES = ascii_lowercase + ascii_uppercase

with open(f"../inputs/{day}.txt") as input:
    lines = [line.strip("\n") for line in input.readlines()]


def part1(lines):
    """Split the line in half and find the common item in each compartment."""
    total_priorities = 0
    for line in lines:
        half = len(line) // 2
        first_compartment = set(line[:half])
        second_compartment = set(line[half:])
        common_item = list(first_compartment & second_compartment)[0]
        total_priorities += PRIORITIES.find(common_item) + 1
    return total_priorities


def part2(lines):
    """Find the common item across three lines."""
    total_priorities = 0
    for group in range(0, len(lines) - 1, 3):
        elf1 = lines[group]
        elf2 = lines[group + 1]
        elf3 = lines[group + 2]
        common_item = list(set(elf1) & set(elf2) & set(elf3))[0]
        total_priorities += PRIORITIES.find(common_item) + 1
    return total_priorities


if __name__ == "__main__":
    from pyperclip import copy

    # copy(part1(lines))
    # copy(part2(lines))
