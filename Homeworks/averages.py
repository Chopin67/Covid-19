def mean(a, b, c):
    return (a+b+c)/3


def median(a, b, c):
    if a <= b <= c:
        return b
    elif c <= b <= a:
        return b
    elif b <= a <= c:
        return a
    elif c <= a <= b:
        return a
    elif a <= c <= b:
        return c
    elif b <= c <= a:
        return c


def rms(a, b, c):
    return (mean(a**2, b**2, c**2))**0.5


def middle_average(a, b, c):
    return median(mean(a, b, c), median(a, b, c), rms(a, b, c))

