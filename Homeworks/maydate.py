# this function computes the upper acceptable range for the younger number
# and the lower acceptable range for the older number
# therefore, if the younger age's upper range is lower than the older range's lower range, then it is creepy

def maydate(x, y):
    '''returns True if x is smaller than y, False if it is not'''
    x = (x*2)-13       # older range for younger age    # x is younger age
    y = (y//2) + 7        # younger range for older age       # y is older age

    return(x < y)


