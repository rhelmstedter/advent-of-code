from aocd import get_data, submit


def get_lines(day: int) -> str:
    """Uses aocd to get the input then splits it into lines."""
    return get_data(day=day, year=2022)


def _parse_diagram(diagram: str) -> dict:
    lines = diagram.split("\n")
    stack_numbers = lines[-1].split()
    stacks = [list() for stack_number in stack_numbers]
    for line in lines[:-1]:
        for stack, crate in enumerate(range(1, len(line), 4)):
            if line[crate] != " ":
                stacks[stack].append(line[crate])
    return {
        int(stack_number): crates[::-1]
        for stack_number, crates in zip(stack_numbers, stacks)
    }


def _parse_move(stacks: dict[list], move: str) -> dict:
    count, start, end = [int(i) for i in move.split() if i.isnumeric()]
    for c in range(count):
        crate = stacks[start].pop()
        stacks[end].append(crate)
    return stacks


def _parse_move_part2(stacks: dict[list], move: str) -> dict:
    count, start, end = [int(i) for i in move.split() if i.isnumeric()]
    crates_to_move = stacks[start][-count:]
    stacks[start] = stacks[start][:-count]
    stacks[end] = stacks[end] + crates_to_move
    return stacks


def part1(lines):
    """ """
    diagram, moves = lines.split("\n\n")
    stacks = _parse_diagram(diagram)
    for move in moves.strip("\n").split("\n"):
        stacks = _parse_move(stacks, move)
    return "".join(stack[-1] for stack in stacks.values())


def part2(lines):
    """ """
    diagram, moves = lines.split("\n\n")
    stacks = _parse_diagram(diagram)
    for move in moves.strip("\n").split("\n"):
        stacks = _parse_move_part2(stacks, move)
    return "".join(stack[-1] for stack in stacks.values())


if __name__ == "__main__":
    day = 5
    lines = get_lines(day)
    # submit(part1(lines), part="a", day=day, year=2022)
    submit(part2(lines), part="b", day=day, year=2022)
