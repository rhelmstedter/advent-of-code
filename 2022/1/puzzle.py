day = 1

with open(f"../inputs/{day}.txt") as input:
    lines = [line.strip("\n") for line in input.readlines()]


def part1(lines):
    """elf with the most calories"""
    elves = []
    current_elf = 0
    for line in lines:
        if line:
            current_elf += int(line)
        else:
            elves.append(current_elf)
            current_elf = 0
    return sorted(elves)


def part2(lines):
    """top 3 from part one"""
    elves = part1(lines)
    return sum(elves[-3:])


if __name__ == "__main__":
    from pyperclip import copy

    # copy(part1(lines)[-1])
    copy(part2(lines))
