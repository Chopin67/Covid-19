# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)
# azh5kn Alexandra Hickman, Amara Vo (av2jf), Tony Albini (apa5dj)
marbles = 0
pick = 0


def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    ans = 1
    while ans <= n and (2**n) - 1 < n//2:
        ans = (2**n) - 1
    return ans

print("The Game of Nim\n")
while marbles <= 0:
    marbles = int(input("The number of marbles in the pile: "))         # cast as an integer so that it can compare
turn_choice = input("Who will start? (p or c): ")
turn = False

if turn_choice == 'p':
    turn = True

while marbles != 0:

    print("The pile has", marbles, "marbles in it.")
    if turn:
        if marbles > 1:
            can_take = marbles // 2
            take = int(input("How many marbles do you want to take (1-" + str(can_take) + "): "))
            marbles -= take

    else:
        take = 1
        target = pow2(marbles)
        take = target
        if take < 1:
            take = 1
        marbles -= take
        print("The computer takes", take, "marbles.")

    turn = not turn
    if marbles == 1:
        break
if turn:
    print("The player wins!")
else:
    print("The computer wins!")
