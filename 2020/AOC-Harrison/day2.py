import argparse
import re
import sys

def eval_line(line):
    '''
    Returns True if the password has the character
    n-m times.  n-m char: pw
    >>> eval_line('1-3 a: abcde')
    True
    >>> eval_line('1-3 b: cdefg')
    False
    '''
    n1,n2 = get_ranges(line)
    char = line.split(' ')[1][:-1]
    pw = line.split(' ')[-1]
    return n1 <= pw.count(char) <= n2


def eval_line_part2(line):
    """
    >>> eval_line_part2('1-3 a: abcde')
    True
    >>> eval_line_part2('1-3 b: cdefg')
    False
    >>> eval_line_part2('2-9 c: ccccccccc')
    False
    """
    n1,n2 = get_ranges(line)
    idx1 = n1-1
    idx2 = n2-1
    char = get_char(line)
    pw = line.split(' ')[-1]
    return (pw[idx1] == char and pw[idx2] != char) or \
        (pw[idx1] != char and pw[idx2] == char) 


def get_char(line):
    """
    >>> get_char('1-3 a: abcde')
    'a'
    >>> get_char('1-3 b: cdefg')
    'b'
    """
    mo = re.search(r'(.):', line)
    return mo.groups()[0]


def get_ranges(line):
    '''
    >>> get_ranges('1-3 a: abcde')
    (1, 3)
    '''
    nums = line.split(' ')[0].split('-')
    return int(nums[0]), int(nums[-1])


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', help='filename to parse')
    ap.add_argument('-p', '--part-two', help='run part2',
                    action='store_true')
    ap.add_argument('-t', '--test', help='run doctest',
                    action='store_true')

    opts = ap.parse_args(args)
    if opts.file:
        lines = open(opts.file, encoding='utf8').read().strip().split('\n')
        if opts.part_two:
            print(sum(eval_line_part2(line) for line in lines))
        else:
            print(sum(eval_line(line) for line in lines))
    if opts.test:
        import doctest
        doctest.testmod()

if __name__ == '__main__':
    main(sys.argv[1:])
