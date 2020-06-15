word = input("Enter a word or phrase: ")    # Ask for word
word_low = word.lower()    # Lower case word
target = "_".join(word_low) + "_"       # Underscores after letters
count_target = target.count('_')
blank = "The word to guess: " + ("_" * count_target) # Counts number of spaces
print(blank)
letter = input("Guess a letter: ")      # Ask user for letter

if letter in target:
    location = target.index(letter)     # letter location
    slice = target[location:location + 2]  # sliced letter + underscore
    newTarget = target.replace(slice, letter * 2)
    newGuess = newTarget[1::2]
    print("The word to guess: " + newTarget[1::2])

if letter in target:
    location = newTarget.index(letter)  # letter location
    slice = newTarget[location:location + 2]  # sliced letter + underscore
    newTarget2 = newTarget.replace(slice, letter * 2)
    newGuess = newTarget[1::2]
    print("The word to guess: " + newTarget[1::2])

if letter in target:
    location = newTarget2.index(letter)  # letter location
    slice = newTarget2[location:location + 2]  # sliced letter + underscore
    newTarget3 = newTarget2.replace(slice, letter * 2)
    newGuess = newTarget2[1::2]
    print("The word to guess: " + newTarget[1::2])

if letter in target:
    location = newTarget3.index(letter)  # letter location
    slice = newTarget3[location:location + 2]  # sliced letter + underscore
    newTarget4 = newTarget3.replace(slice, letter * 2)
    newGuess = newTarget3[1::2]
    print("The word to guess: " + newTarget[1::2])

