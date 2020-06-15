# Alex Hickman azh5kn Amara Vo av2jf


def ellipsis(s):

    first_two = s[0:2]
    middle = s[2:-2]  # what we want to change
    last_two = s[-2:]
    return first_two+"..."+last_two


def eighteen(s):
    first_one = s[0:1]
    middle = (len(s)-2)
    last_one = s[-1:]
    return first_one+str(middle)+last_one

def allit(s, t):
    s = s.capitalize()
    print(s)
    t = t.capitalize()
    print(t)
    vowel = "aeiou"  # "a" or "e" or "i" or "o" or "u"
    vowelscap = vowel.capitalize()
    if s[0:1] == t[0:1] and (s[0:1] and t[0:1] != vowel or vowelscap):
        return True
    else:
        return False
print(allit("eat", "eotton"))



