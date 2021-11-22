import re
from operator import add, sub, mul, floordiv
from functools import reduce


def answer(question):

    PARSE_REGEX = r'What is (-?[0-9]+)(( (?:plus|minus|multiplied by|divided by) (?:-?[0-9]+))*)\?'
    REPEAT_GROUPS = r' (plus|minus|multiplied by|divided by) (-?[0-9]+)'

    match = re.match(PARSE_REGEX, question)
    if match:
        first, others, *_ = match.groups()
    else:
        raise ValueError('Invalid input')

    others = re.findall(REPEAT_GROUPS, others)

    lookup = {
        'plus': add,
        'minus': sub,
        'multiplied by': mul,
        'divided by': floordiv
    }

    return reduce(
        lambda total, pair: lookup[pair[0]](total, int(pair[1])),
        others,
        int(first)
    )