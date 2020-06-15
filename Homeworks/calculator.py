# azh5kn Alexandra Hickman Calculator


def binop(math_string):

    multiplication = math_string.find('*')
    addition = math_string.find('+')
    subtraction = math_string.find('-')
    division = math_string.find('/')

    if multiplication > 0:
        number_one = int(math_string[0:multiplication])
        number_two = int(math_string[multiplication + 1:])
        return number_one * number_two
    elif addition > 0:
        number_one = int(math_string[0:addition])
        number_two = int(math_string[addition + 1:])
        return number_one + number_two
    elif subtraction > 0:
        number_one = int(math_string[0:subtraction])
        number_two = int(math_string[subtraction + 1:])
        return number_one - number_two
    elif division > 0:
        number_one = int(math_string[0:division])
        number_two = int(math_string[division + 1:])
        return number_one / number_two

