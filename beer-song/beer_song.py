def recite(start, take=1):
    song = [verse(n) + [""] for n in range(start, start - take, -1)]
    return [line for v in song for line in v][:-1]


def verse(n):
    return [
        f"{beer(n).capitalize()} on the wall, {beer(n)}.",
        (f"Take {'one' if n>1 else 'it'} down and pass it around" if n else "Go to the store and buy some more") + f", {beer(n-1)} on the wall."
    ]


def beer(n):
    return f"{'99' if n == -1 else n if n else 'no more'} bottle{'s' if n!=1 else ''} of beer"
