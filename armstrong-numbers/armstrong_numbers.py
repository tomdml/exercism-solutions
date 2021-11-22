def is_armstrong_number(number):
    strlen = len(str(number))
    return number == sum(int(d) ** strlen for d in str(number))
