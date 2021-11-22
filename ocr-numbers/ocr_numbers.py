numberString = [
    ' _     _  _     _  _  _  _  _ ',
    '| |  | _| _||_||_ |_   ||_||_|',
    '|_|  ||_  _|  | _||_|  ||_| _|',
    '                              ',
]


def convert(input_grid):
    numbers = dict(zip(grouper(numberString), '0123456789'))
    numbers[','] = ','

    if len(input_grid) % 4 or any(len(line) % 3 for line in input_grid):
        raise ValueError('Invalid input shape!')

    return ''.join(numbers.get(g, '?') for g in grouper(input_grid)).strip(',')


def grouper(grid):
    for i in range(0, len(grid), 4):
        lines = grid[i: i + 4]
        for j in range(0, len(lines[0]), 3):
            yield ''.join(''.join(line[j: j + 3]) for line in lines)
        yield ','
