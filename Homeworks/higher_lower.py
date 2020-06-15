#azh5kn Alexandra Hickman

import random
correct_answer = int(input("What should the answer be?: "))
correctt_answer = str(correct_answer)
guesses = int(input("How many guesses?: "))
integer = type(int)
answer = int(input("Guess a number: "))

if correct_answer == -1:
    correct_answer = random.randrange(1, 100)
    correctt_answer = str(correct_answer)

while guesses > 1:

    if answer == correct_answer:
        print("You win!")
        guesses = 7             # set to random positive number to make it work
        break
    elif answer > correct_answer:
        print("The number is lower than that.")
        answer = int(input("Guess a number: "))
        guesses = guesses -1
    elif answer < correct_answer:
        print("The number is higher than that.")
        answer = int(input("Guess a number: "))
        guesses = guesses - 1

while guesses == 1:
    if answer == correct_answer:
        print("You win!")
        break
    else:
        print("You lose; the number was "+correctt_answer)
        break


