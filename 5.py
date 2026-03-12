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


def pig_latin2a(word): # TODO clean that up
    capitalize = word[0].isupper()
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    punctuation = ['.', ',', '?', '!']
    punct = word[-1] in punctuation
    if punct: word = word[:-1]
    if word[0] in vowels:
        word = word.lower()
        word = f"{word}way"
    else: word = f"{word[1:]}{word[0]}ay"

    if capitalize: word = word.capitalize()
    if punct: word = f"{word}."
    return word


def pig_latin2b(word): # TODO clean that up
    capitalize = word[0].isupper()
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} # made it a set here
    punctuation = ['.', ',', '?', '!']
    punct = word[-1] in punctuation
    if punct: word = word[:-1]
    if(len(set(word) & vowels)>=2):
        word = word.lower()
        word = f"{word}way"
    else: word = f"{word[1:]}{word[0]}ay"

    if capitalize: word = word.capitalize()
    if punct: word = f"{word}."
    return word

# print(pig_latin2b("wine"))
# print(pig_latin2b("wind"))

# 6 Do it for a sentence

def pl_sentence(str):
    str_list = str.split(" ")
    for i, _ in enumerate(str_list):
        print(pig_latin2a(str_list[i]), end =" ")

def pl_sentence2(str):
    output = []
    for word in str.split(" "):
        if word[0] in 'aeiou':
            output.append(f"{word}way")
        else: output.append(f"{word[1:]}{word[0]}ay")
    return ' '.join(output)


sentence = "this is a test translation"
print(pl_sentence2(sentence))

