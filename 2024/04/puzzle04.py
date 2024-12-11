import aocd


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2024).splitlines()
    else:
        return aocd.get_data(day=day, year=2024)


def part1(data):
    """ """
    HEIGHT = len(data)
    WIDTH = len(data[0])
    found = 0
    for row in range(HEIGHT):
        for col in range(WIDTH):
            horizontal, h = "", "h"
            vertical, v = "", "v"
            backward_diagonal, b = "", "b"
            forward_diagonal, f = "", "f"

            if col <= WIDTH - 4:
                horizontal = data[row][col : col + 4]

            if row <= HEIGHT - 4:
                for i in range(row, row + 4):
                    vertical += data[i][col]

            if row <= HEIGHT - 4 and col >= 3:
                for i in range(4):
                    backward_diagonal += data[row + i][col - i]

            if row <= HEIGHT - 4 and col <= WIDTH - 4:
                for i in range(4):
                    forward_diagonal += data[row + i][col + i]

            for dir, short in zip(
                (horizontal, vertical, backward_diagonal, forward_diagonal),
                (h, v, b, f),
            ):
                if dir == "XMAS" or dir == "SAMX":
                    print("found:", short, f"at {row=}, {col=}")
                    found += 1
    return found


CORNERS = (
    (-1, -1),  # up/left
    (-1, 1),  # up/right
    (1, -1),  # down/left
    (1, 1),  # down/right
)


def part2(data):
    """ """
    HEIGHT = len(data)
    WIDTH = len(data[0])
    found = 0
    for row in range(1, HEIGHT - 1):
        for col in range(1, WIDTH - 1):
            if data[row][col] == "A":
                corner_chars = []
                for corner in CORNERS:
                    corner_chars.append(data[row + corner[0]][col + corner[1]])
                if (corner_chars[0] == "S" and corner_chars[3] == "M") or (
                    corner_chars[0] == "M" and corner_chars[3] == "S"
                ):
                    if (corner_chars[1] == "S" and corner_chars[2] == "M") or (
                        corner_chars[1] == "M" and corner_chars[2] == "S"
                    ):
                        found += 1
    return found


if __name__ == "__main__":
    day = 4
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2024)
    # aocd.submit(part2(data), part="b", day=day, year=2024)
