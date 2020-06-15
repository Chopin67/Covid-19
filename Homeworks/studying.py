def f(g):
    global h
    g = g + g
    h = g
    print(g)
    print(h)
g = "3"
h = 4
f(g)
print(g)
print(h)
