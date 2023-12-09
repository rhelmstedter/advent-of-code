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
        if param in range(m.source, m.source + m._range):
            return param - m.source + m.destination
    return param


def rev_mapper(param, map: list[Mapping]):
    for m in map:
        if param in range(m.destination, m.destination + m._range):
            return param + m.source - m.destination
    return param


def start_to_end(seed, maps):
    next = seed
    for map in maps.values():
        result = _mapper(next, map)
        next = result
    return result


def end_to_start(seed, maps):
    next = seed
    for map in reversed(maps.values()):
        result = rev_mapper(next, map)
        next = result
    return result


def part1(data):
    """ """
    seeds, maps = _parser(data)
    locations = []
    for seed in seeds:
        locations.append(start_to_end(seed, maps))
    return min(locations)


def reverse_lookup_seed(location: int, maps: dict[str, list[Mapping]]) -> int:
    value = location
    for current_map in reversed(maps.values()):
        value = next(
            (
                m.source + (value - m.destination)
                for m in current_map
                if value in range(m.destination, m.destination + m._range)
            ),
            value,  # fallback
        )
    return value


def part2(data):
    """Tried reverse mapping. That didn't work either."""

    seeds, maps = _parser(data)
    print(maps)
    seed_ranges = [
        range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
    ]
    location = 0
    while True:
        potential_seed = reverse_lookup_seed(location, maps)
        if any(potential_seed in seed_range for seed_range in seed_ranges):
            return location
        location += 1


if __name__ == "__main__":
    day = 5
    data = get_data(day)
    # aocd.submit(part1(data), part="a", day=day, year=2023)
    # aocd.submit(part2(data), part="b", day=day, year=2023)
