# azh5kn Alexandra Hickman    and     av2jf Amara Vo
# not finished
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def index_to_letter(index):
    letter = alphabet[index]
    return letter

def letter_to_index(letter):
    letter_cap = letter.capitalize()
    index = alphabet.find(letter_cap)
    return index


def is_letter(letter):
    letter_cap = letter.capitalize()
    if letter_cap in alphabet:
        return True

def interleave(string):
    newText = string.strip()
    if (len(newText)%2) == 0:
        first_half = newText[0:(len(newText)//2)]
        second_half = string[(len(newText)//2):]
    else:
        first_half = newText[0:((len(newText) // 2)+1]
        second_half = string[((len(newText) // 2)+1:]

    for char in first_half:
        second_letter = second_half[0]
        third_letter


print(index_to_letter(-2))
print(letter_to_index('z'))
print(is_letter('S'))
print(interleave("1234567"))

