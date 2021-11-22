scores = (
    ('AEIOULNRST', 1), ('DG', 2), ('BCMP', 3),
    ('FHVWY', 4), ('K', 5), ('JX', 8), ('QZ', 10))
scoredict = {char: value for score, value in scores for char in score}


def score(word):
    return sum(scoredict[w] for w in word.upper())
