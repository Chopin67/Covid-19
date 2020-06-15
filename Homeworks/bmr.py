# azh5kn Alexandra Hickman
# If input is "female" the value will be -161
# If not, the value will be 5


def st_jeor(mass, height, age, sex):
    if sex == 'female':
        sex = -161
    elif sex == 'male':
        sex = 5
    return (10.0*mass)+(6.25*height)-(5.0*age)+sex



