from itertools import permutations


def rectangles(strings):
    corners = [
        (x, y)
        for y, row in enumerate(strings)
        for x, c in enumerate(row)
        if c == '+'
    ]

    possible = [
        ((x1, y1), (x2, y2))
        for (x1, y1), (x2, y2)
        in permutations(corners, 2)
        if x1 < x2 and y1 < y2
    ]

    count = 0
    for (x1, y1), (x2, y2) in possible:
        vert = set(
            strings[y1][x1: x2 + 1] +
            strings[y2][x1: x2 + 1]
        )
        horiz = set(
            (strings[y][x1] for y in range(y1, y2 + 1)) +
            (strings[y][x2] for y in range(y1, y2 + 1))
        )

        count += all((
            ' ' not in vert | horiz,
            '|' not in vert,
            '-' not in horiz
        ))

    return count
