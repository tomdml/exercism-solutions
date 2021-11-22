from collections import Counter


def YACHT(x): return 50 * (x == x[::-1])
def ONES(x): return 1 * x.count(1)
def TWOS(x): return 2 * x.count(2)
def THREES(x): return 3 * x.count(3)
def FOURS(x): return 4 * x.count(4)
def FIVES(x): return 5 * x.count(5)
def SIXES(x): return 6 * x.count(6)
def LITTLE_STRAIGHT(x): return 30 if set(x) == {1, 2, 3, 4, 5} else 0
def BIG_STRAIGHT(x): return 30 if set(x) == {2, 3, 4, 5, 6} else 0
def CHOICE(x): return sum(x)

def FULL_HOUSE(x):
    _, c = zip(*Counter(x).most_common(2))
    if c == (3, 2):
        return sum(x)
    else:
        return 0
        
def FOUR_OF_A_KIND(x):
    n, c = zip(*Counter(x).most_common(1))
    print(c)
    if c[0] >= 4:
        return 4 * n[0]
    else:
        return 0


def score(dice, category):
    return category(dice)
