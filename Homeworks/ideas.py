#azh5kn Alexandra Hickman
max = 100
min = 1
print("Think of a number between 1 and 100 and I'll guess it.")
guesses = int(input("How many guesses do I get? "))
won = False
while guesses >= 1 and not won:
    middle = (max+min)//2
    h_l = input("Is the number higher, lower, or the same as " + str(middle) + "? ")
    if
    if  h_l == "higher":
        min = middle
        guesses = guesses - 1
    if h_l ==  "lower":
        max = middle
        guesses = guesses - 1
    if h_l == "same":
        print("I won!")
        won = True

if not won:
    actual_answer = int(input("I lost; what was the answer? "))
    if actual_answer <= min:
        print("That can't be; you said it was higher than "+str(min)+ "!")
    elif actual_answer >= max:
        print("That can't be; you said it was lower than "+str(max)+ "!")
    else:
        print("Well played!")
