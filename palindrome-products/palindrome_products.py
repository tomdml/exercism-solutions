def largest(min_factor, max_factor):
    return smallest(min_factor, max_factor, step=-1)


def smallest(min_factor, max_factor, step=1):
    rng = range(min_factor**2, max_factor**2 + 1) if step == 1 else range(max_factor**2, min_factor**2 - 1, -1)
    for i in rng:
        if str(i) == str(i)[::-1]:
            facs = [(f, i / f) for f in factors(i) if min_factor <= f <= max_factor]
            if facs:
                return facs


def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n // i)
    )
