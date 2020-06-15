integer = int(input("Enter an integer: "))
roman_numbers = ["I", "V", "X", "L", "C", "D", "M"]
odd_cases = [1, 5, 10, 50, 100, 500, 1000]
other_cases = [4, 9]
if integer > 3999 or integer < 1:
    print("Input must be between 1 and 3999")

while 0 < integer < 4000:
    number_of_M = integer // (odd_cases[6])
    roman = ""
    if number_of_M > 0:
        number_of_D = (integer - number_of_M * 1000) // odd_cases[5]
        roman = roman + (roman_numbers[6] * number_of_M)
        integer = integer - number_of_M * 1000

    elif number_of_M == 0:
        number_of_D = integer // odd_cases[5]

    if number_of_D > 0:
        number_of_C = (integer - number_of_D * 500) // odd_cases[4]
        integer = integer - number_of_D * 500
        if number_of_D == 1 and number_of_C == 4:
            roman = roman + roman_numbers[4]+roman_numbers[6]
        else:
            roman = roman + (roman_numbers[5] * number_of_D)
    elif number_of_D == 0:
        number_of_C = integer // odd_cases[4]

    if number_of_C > 0:
        number_of_L = (integer - number_of_C * 100) // odd_cases[3]

        integer = integer - number_of_C * 100
        if number_of_C == 4:
            if number_of_D == 1:
                roman = roman
            else:
                roman = roman + roman_numbers[4] + roman_numbers[5]
        else:
            roman = roman + (roman_numbers[4] * number_of_C)
    elif number_of_C == 0:
        number_of_L = integer // odd_cases[3]

    if number_of_L > 0:
        number_of_X = (integer - number_of_L * 50) // odd_cases[2]

        integer = integer - number_of_L * 50
        if number_of_L == 1 and number_of_X == 4:
            roman = roman + roman_numbers[2]+roman_numbers[4]
        else:
            roman = roman + (roman_numbers[3] * number_of_L)
    elif number_of_L == 0:
        number_of_X = integer // odd_cases[2]

    if number_of_X > 0:
        number_of_V = (integer - number_of_X * 10) // odd_cases[1]
        integer = integer - number_of_X * 10
        if number_of_X == 4:
            if number_of_L == 1:
                roman = roman
            else:
                roman = roman + roman_numbers[2] + roman_numbers[3]
        else:
            roman = roman + (roman_numbers[2] * number_of_X)
    elif number_of_X == 0:
        number_of_V = integer // odd_cases[1]

    if number_of_V > 0:
        number_of_I = (integer - number_of_V * 5) // odd_cases[0]
        integer = integer - number_of_V * 5

        if number_of_V == 1 and number_of_I == 4:
            roman = roman + roman_numbers[0]+roman_numbers[2]
            number_of_I = 0
        else:
            roman = roman + (roman_numbers[1] * number_of_V)

    elif number_of_V == 0:
        number_of_I = integer // odd_cases[0]


    if number_of_I > 0:

        if number_of_I == 4:
            roman = roman + roman_numbers[0]+roman_numbers[1]
        else:
            roman = roman + (roman_numbers[0] * number_of_I)

    print(roman)
    break



