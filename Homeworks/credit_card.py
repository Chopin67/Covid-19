def check(integer):
    empty = ''
    every_other = []
    total = 0
    sum = 0
    integer = str(integer)
    if len(integer)%2 == 0:
        for i in range(1, len(integer), 2):         # every other number
            number = (integer[i])
            every_other.append(number)
    else:
        for i in range(0, len(integer), 2):
            number = (integer[i])
            every_other.append(number)

    for j in every_other:                       # sum of every other number
        j = int(j)
        total += j

    if len(integer)%2 == 0:
        for l in range(0, len(integer), 2):
            other_number = int(integer[l])
            other_number = other_number * 2
            empty = empty + str(other_number)
    else:
        for l in range(1, len(integer), 2):
            other_number = int(integer[l])
            other_number = other_number * 2
            empty = empty + str(other_number)

    for m in empty:                       # sum of every other number
       m = int(m)
       sum += m

    sum_of_both = total + sum
    sum_of_both = str(sum_of_both)
    see = int(sum_of_both[len(sum_of_both) - 1])
    if see == 0 and len(sum_of_both) > 1:
        # return 'GOOD:'+integer+' is valid'
        return True
    else:
       # return 'ERROR:'+ integer+' is not valid'
       return False







