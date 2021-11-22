def annotate(minefield):

    if minefield == []:
        return []

    if len(set(len(row) for row in minefield)) != 1:
        raise ValueError('Non-rectangular minefield!')

    if any(c not in ' *' for row in minefield for c in row):
        raise ValueError('Bad character!')

    mines = {
        (x, y)
        for y, row in enumerate(minefield)
        for x, char in enumerate(row)
        if char == '*'
    }

    return [
        ''.join(nbors(x, y, mines) if char == ' ' else '*'
                for x, char in enumerate(row))
        for y, row in enumerate(minefield)
    ]


def nbors(x, y, mines):

    coords = {
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    }

    count = len(coords & mines)
    return str(count) if count else ' '
