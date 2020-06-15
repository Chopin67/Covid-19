x = [1, 2, "three"]
y = x#[:]
y = 2*x
x = 2*x
x[1] = 11
# y = [4, 5, 6]
print(x)
print(y)
 