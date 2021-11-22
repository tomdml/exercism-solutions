def value(colors):
    values = "black brown red orange yellow green blue violet grey white".split()
    return 10 * values.index(colors[0]) + values.index(colors[1])

    # return int(''.join(str(values.index(color)) for color in colors[:2]))
