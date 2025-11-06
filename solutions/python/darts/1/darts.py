def score(x, y):
    if 0 <= x**2 + y**2 <= 1:
        return 10
    if 1 < x**2 + y**2 <= 25:
        return 5
    if 25 < x**2 + y**2 <= 100:
        return 1
    return 0
        