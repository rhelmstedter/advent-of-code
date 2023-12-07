from collections import defaultdict
from dataclasses import dataclass

import aocd
from rich import print
from rich.progress import track


def get_data(day: int, lines: bool = True) -> str | list:
    """Uses aocd to get the input then splits it into lines."""
    if lines:
        return aocd.get_data(day=day, year=2023).splitlines()
    else:
        return aocd.get_data(day=day, year=2023)


@dataclass
class Mapping:
    destination: int
    source: int
    _range: int


def _parser(data) -> tuple[list[int], dict[str, Mapping]]:
    seeds = [int(seed) for seed in data[0].split()[1:]]
    maps = defaultdict(list)
    new_map = False
    for line in data[1:]:
        if not line:
            new_map = True
            continue
        if new_map:
            description = line.strip(":")
            new_map = False
            continue
        maps[description].append(Mapping(*(int(s) for s in line.split())))
    return seeds, maps


def _mapper(param, map: list[Mapping]):
    for m in map:
        if param in range(m.source, m.source + m._range + 1):
            if m.source > m.destination:
                return param - (m.source - m.destination)
            if m.source < m.destination:
                return param + (m.destination - m.source)
    return param


def start_to_end(seed, maps):
    next = seed
    for map in maps.values():
        result = _mapper(next, map)
        next = result
    return result


def part1(data):
    """ """
    seeds, maps = _parser(data)
    locations = []
    for seed in seeds:
        locations.append(start_to_end(seed, maps))
    return min(locations)


def part2(data):
    """This doesn't work, you know because the numbers are real big."""
    seeds, maps = _parser(data)
    locations = []
    for idx in track(range(0, len(seeds), 2)):
        for seed in range(seeds[idx], seeds[idx] + seeds[idx + 1] + 1):
            locations.append(start_to_end(seed, maps))
    return min(locations)


if __name__ == "__main__":
    day = 5
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
