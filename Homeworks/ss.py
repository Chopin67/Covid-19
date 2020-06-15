def norm_num(num):
    num_float = float(num)
    num_int = int(num_float)

    if num_float == num_int:
        return num_int
    else:
        return num_float

print(norm_num('2.0'))
