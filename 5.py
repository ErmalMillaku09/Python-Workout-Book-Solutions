def pig_latin(word):
    """If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay"""
    cap_first = False
    if word[0].isupper():
        word = word.lower()
        cap_first=True
    if word[0] in 'aeiou':
        word = f"{word}way"
        if cap_first:
            word = word.capitalize()
        return word
    word = f"{word[1:]}{word[0]}ay"
    if cap_first:
       word = word.capitalize()
    return word

def pig_latin2(word):
    """If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay"""
    cap_first = False
    if word[-1] in ".,?!":
        c = word[-1]
        word = word[:-1]
    if word[0].isupper():
        word = word.lower()
        cap_first=True
    if word[0] in 'aeiou':
        word = f"{word}way"
        if cap_first:
            word = word.capitalize()
        if c:
            word = word + c
        return word
    word = f"{word[1:]}{word[0]}ay"
    if c:
        word = word + c
    if cap_first:
       word = word.capitalize()
    return word


pig_latin2a(): # TODO clean that up

print(pig_latin2("air."))
print(pig_latin2("Computer."))
print(pig_latin2("Air."))
print(pig_latin2("computer."))