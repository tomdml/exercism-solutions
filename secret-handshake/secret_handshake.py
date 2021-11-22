def commands(number):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    binstring = format(number, 'b')[::-1]
    result = [a for a, b in zip(actions, binstring) if int(b)]
    return result[::-1] if number & 10000 else result
