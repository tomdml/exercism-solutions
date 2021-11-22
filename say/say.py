digits = '. one two three four five six seven eight nine'.split()
teens = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
multiples = '. . twenty thirty forty fifty sixty seventy eighty ninety'.split()


def triplet(s):
    huns, tens, units = s

    huns = f'{digits[int(huns)]} hundred' if huns != '0' else ''

    if tens + units == '00':
        others = ''
    elif tens == '1':
        others = teens[int(units)]
    else:
        tens = multiples[int(tens)] if tens != '0' else ''
        units = digits[int(units)] if units != '0' else ''
        others = '-'.join(word for word in (tens, units) if word)

    return ' '.join(word for word in (huns, others) if word)


def say(num):
    if not 0 <= num <= 999_999_999_999:
        raise ValueError('Number out of range')

    if num == 0:
        return 'zero'

    num = format(num, '012')
    bils, mils, thous, ones = num[:3], num[3:6], num[6:9], num[9:]

    result = [triplet(s) + qty
              for s, qty
              in zip(
                  (bils, mils, thous, ones),
                  (' billion', ' million', ' thousand', ''))
              if int(s)]

    return ' '.join(result)
