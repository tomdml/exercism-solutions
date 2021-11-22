def score(x, y):
    distance = (x**2 + y**2)**0.5
    return (0 if distance > 10
            else 1 if distance > 5
            else 5 if distance > 1
            else 10)
