test = """199 200 208 210 200 207 240 269 260 263""".split()

with open("inputs/day1.txt", "r", encoding="utf8") as p_input:
    sonar_sweeps = p_input.readlines()


def two_sliding_window(sweeps):
    count = 0
    for current_line, next_line in zip(sweeps, sweeps[1:]):
        if int(current_line) < int(next_line):
            count += 1
    return count


def three_measurement_zip(sweeps):
    windows = []
    for (
        pane1,
        pane2,
        pane3,
    ) in zip(sweeps, sweeps[1:], sweeps[2:]):
        window = sum([int(pane1), int(pane2), int(pane3)])
        windows.append(window)
    return windows


def three_sliding_window(sweeps):
    count = 0
    for i in range(len(sweeps) - 3):
        window1 = sum(
            [
                int(sweeps[i]),
                int(sweeps[i + 1]),
                int(sweeps[i + 2]),
            ]
        )
        window2 = sum(
            [
                int(sweeps[i + 1]),
                int(sweeps[i + 2]),
                int(sweeps[i + 3]),
            ]
        )
        if window2 > window1:
            count += 1
    return count


print(f"Part 1: {two_sliding_window(sonar_sweeps)}")
print(f"Part 2: {three_sliding_window(sonar_sweeps)}")
print(f"Part2 funcs: {two_sliding_window(three_measurement_zip(sonar_sweeps))}")
