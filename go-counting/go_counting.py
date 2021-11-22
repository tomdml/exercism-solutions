from collections import defaultdict

BLACK, WHITE, NONE = 'B', 'W', ''


class Board:
    def __init__(self, board):
        self.board = board

    def _validate(self, x, y):
        return 0 <= x < len(self.board[0]) and 0 <= y < len(self.board)

    def territory(self, x, y):
        if not self._validate(x, y):
            raise ValueError('Invalid input!')

        visited, stones = set(), set()
        neighbours = ((1, 0), (0, 1), (-1, 0), (0, -1))

        notvisited = [(x, y)]
        while notvisited:
            x, y = notvisited.pop()
            val = self.board[y][x]
            if val == ' ':
                visited.add((x, y))
                for dx, dy in neighbours:
                    newX, newY = x + dx, y + dy
                    if (newX, newY) not in visited and self._validate(newX, newY):
                        newval = self.board[newY][newX]
                        if newval == ' ':
                            notvisited.append((newX, newY))
                        else:
                            stones.add(newval)
                            
        owner = list(stones)[0] if len(stones) == 1 else ''
        return (owner, visited)

    def territories(self):
        result = defaultdict(set)
        for (y, row) in enumerate(self.board):
            for (x, val) in enumerate(row):
                if val == ' ':
                    owner, _ = self.territory(x, y)
                    result[owner].add((x, y))
        return result
