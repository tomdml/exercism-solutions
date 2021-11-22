from collections import Counter, defaultdict
from itertools import count

acetoace = (
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

cardscore = dict(zip(
    acetoace[1:],
    count(start=2)
))


def score(hand):
    nums, suits = [], []
    for card in hand.split():
        nums.append(card[:-1])
        suits.append(card[-1])

    counts = Counter(nums).most_common()

    # Straight Flush - 1
    flushSets = [set(acetoace[i: i + 5]) for i in range(0, len(acetoace) - 4)]
    if len(set(suits)) == 1 and any(set(nums) == g for g in flushSets):
        return (-1, max(nums, key=lambda c: cardscore[c]))

    # Four Kind - 2
    if counts[0][1] == 4:
        return (-2, cardscore[counts[0][0]], cardscore[counts[1][0]])

    # Full House - 3
    if counts[0][1] == 3 and counts[1][1] == 2:
        return (-3, cardscore[counts[0][0]], cardscore[counts[1][0]])

    # Flush - 4
    if len(set(suits)) == 1:
        return (-4,) + tuple(sorted(nums, key=lambda c: cardscore[c]))

    # Straight - 5
    if set(nums) == set('A2345'):
        return (-5, 5)

    if any(set(nums) == g for g in flushSets):
        return (-5,) + tuple(sorted((cardscore[c] for c in nums), reverse=True))

    # Three Kind - 6
    if counts[0][1] == 3:
        return (-6, cardscore[counts[0][0]],
                cardscore[counts[1][0]], cardscore[counts[2][0]])

    # Two Pair - 7
    if counts[0][1] == 2 and counts[1][1] == 2:
        a, b = sorted((cardscore[c[0]] for c in counts[:2]), reverse=True)
        return (-7, a, b, cardscore[counts[2][0]])

    # One Pair - 8
    if counts[0][1] == 2:
        return (-8, cardscore[counts[0][0]],
                cardscore[counts[1][0]],
                cardscore[counts[2][0]], cardscore[counts[3][0]])

    return (-9,) + tuple(sorted((cardscore[c] for c in nums), reverse=True))


def best_hands(hands):
    if len(hands) == 1:
        return hands

    scores = defaultdict(list)
    for hand in hands:
        print(score(hand))
        scores[score(hand)].append(hand)
    return scores[max(scores)]
