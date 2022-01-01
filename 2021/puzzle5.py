from dataclasses import dataclass

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

def parse_line(line):
    '''
    >>> parse_line('1,1 -> 1,3')
    (1, 1, 1, 3)
    '''
    start, _, end = line.split() 
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    return int(x1), int(y1), int(x2), int(y2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


