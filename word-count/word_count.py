import re
from collections import Counter


def count_words(sentence):
    clean = re.sub(r"[^'\w]|_", ' ', sentence.lower())
    words = [w.strip("'")
            for w in clean.split()
            if w]
    return Counter(words)
    