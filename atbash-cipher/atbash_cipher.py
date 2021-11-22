from string import ascii_lowercase

cipher = dict(zip(ascii_lowercase + ' 0123456789',
                  ascii_lowercase[::-1] + ' 0123456789'))


def grouper(it, size):
    for pos in range(0, len(it), size):
        yield ''.join(it[pos:pos + size])


def encode(plain_text):
    return ' '.join(
        grouper([cipher[c] for c in plain_text.lower() if c.isalnum()], 5)
    )


def decode(ciphered_text):
    return ''.join(cipher[c] for c in ciphered_text.lower() if c != ' ')
