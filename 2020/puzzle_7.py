from pyperclip import copy


def parse_line(line):
    """
    >>> test_bag = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    >>> parse_line(test_bag)
    {'light red': ['bright white', 'muted yellow', 'muted yellow']}

    >>> no_bags = 'dotted black bags contain no other bags.'
    >>> parse_line(no_bags)
    {'dotted black': []}
    """

    color, other = line.split(" bags contain ")
    others = other.split(", ")

    result = {}
    for bag_info in others:
        if "no other" in line:
            result[color] = []
            continue
        count = int(bag_info.split()[0])
        other_color = " ".join(bag_info.split()[1:-1])
        if color not in result:
            result[color] = [other_color] * count
        else:
            result[color].extend([other_color] * count)
    return result


def bfs(mapping, root, needle):
    if root == needle:
        return False
    q = []
    discovered = {root}
    q.append(root)
    while q:
        v = q.pop(0)
        if v == needle:
            return True
        for child in mapping.get(v, []):
            if child not in discovered:
                discovered.add(child)
                q.append(child)


def bft(mapping, root):
    q = []
    q.append(root)
    while q:
        v = q.pop(0)
        yield v
        for child in mapping.get(v, []):
            q.append(child)


def traverse_mapping(mapping, needle=None):
    count = 0
    for key in mapping:
        if bfs(mapping, key, needle):
            count += 1
    return count


def traverse_mapping_part2(mapping):
    count = 0
    for key in mapping:
        if bft(mapping, key):
            count += 1
    return count


def part_1():
    with open("inputs/day_7_input.txt", "r") as input:
        lines = input.readlines()
        mapping = {}
        for line in lines:
            mapping.update(parse_line(line))
        total = traverse_mapping(mapping, needle="shiny gold")
        print(total)
        copy(total)


def part_2():
    with open("inputs/day_7_input.txt", "r") as input:
        lines = input.readlines()
        mapping = {}
        for line in lines:
            mapping.update(parse_line(line))
        total = traverse_mapping_part2(mapping, needle="shiny gold")
        print(total)
        copy(total)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    part_1()
    part_2()
