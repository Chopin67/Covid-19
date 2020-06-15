def quad(x, a, b, c):
    # print(a, x**2, '+', b, x, 'x', c, '=',a * x**2+ b * x + c,)
    return a * x**2+ b * x + c

def f(x):
    y = quad(x, 1, -1, -1)
    return y

print(quad(2, 1, 3, 5))
print(f(1.6))

