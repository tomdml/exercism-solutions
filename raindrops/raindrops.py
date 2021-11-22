def convert(number):
    facres = {3: 'Pling',
              5: 'Plang',
              7: 'Plong'}

    result = ''.join(res for (fac, res) in facres.items() if number % fac == 0)

    return result if result else str(number)
