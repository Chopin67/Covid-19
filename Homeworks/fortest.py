def example(shape, length):
    if shape == 'triangle':
        return "The triangle's perimeter is " + str(length*3) + '.'
    elif shape == 'square':
        return "The square's perimeter is "+ str(length*4)+' .'
    elif shape == 'pentagon':
        return "The pentagon's perimeter is "+ str(length*5)+' .'

print(example('pentagon', 2))
