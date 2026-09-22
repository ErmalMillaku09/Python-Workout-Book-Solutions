import string


def pig_latin(word):
    """If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay"""
    cap = False
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # word = list(word)
    c=""
    if word[-1] in ".,?!;":
        c = word[-1]
        word = word[:-1]
    if word[0].isupper():
        cap = True
        word = word.lower()
    if word[0] in vowels:
      word =  (f'{word}way')
    else:
        word = f'{word[1:]}{word[0]}ay'
    if cap:
        word = word.capitalize()

    word = f'{word}{c}'
    return word

def pl_sentence(sentence):
    sentence = sentence.split(' ')
    new_sentence = []
    for i in sentence:
        new_sentence.append(pig_latin(str(i)))
    new_sentence = ' '.join(new_sentence)
    print(new_sentence)

def ub(word):
    word = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for index, element in enumerate(word):
        if element in vowels:
            word[index] = f'ub{word[index]}'
    word = ''.join(word)
    return word

def ub_sentence(sentence):
    sentence = sentence.split(' ')
    new_sentence = []
    for i in sentence:
        new_sentence.append(ub(i))

    new_sentence = ' '.join(new_sentence)
    return new_sentence

text = "According to Smith, the theory was first proposed by Smith in 1905. Later, Smith revised the theory. Many researchers disagreed with Smith."

author = "Smith"

def remove_author(author, text):
    result = []
    for word in text.split(" "):
        if word.strip(string.punctuation) == author:
            result.append("_")
        else:
            result.append(word)
    return ' '.join(result)

# ASCII only letters and numbers 48 57, 65 - 90, 97 - 122
def format_url(url):
    tokenize = list(url)

    for index, char in enumerate(tokenize):
        order = ord(char)
        if order not in range(48,58) and order not in range(65,91) and order not in range(97,123):
            tokenize[index] = f'%{char[2:0]}'
    return ''.join(tokenize)


# [ do this for that in ]

numbers = [1, 2, 3, 4, 5]

newlist = [x * 10 for x in numbers]

evenlist = [x for x in numbers if x % 2 ==0]

listuple = [(x,x*10) for x in numbers]

names = ["John", "Alice", "Bob"]

nametuple = [(x,len(x)) for x in names]

numbers = [1, 2, 3, 4]

numbers = tuple(x*2 for x in numbers )

numbers = [5, 10, 15]

numbers = tuple(x**2 for x in numbers)

list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]
newtuple = tuple((list1[i], list2[i]) for i in range(len(list1)))

newtuple2 = tuple((list1[i], list2[i], list3[i]) for i in range(len(list1)))

lists = (
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300]
)



lists = (
    ["a", "b", "c", "d"],
    [10, 20, 30, 40],
    ["X", "Y", "Z", "W"]
)

result = [tuple(it[i] for it in lists) for i in range(len(lists[0]))]




for i in range(len(lists[0])):
    temp=[]
    for it in lists:
        temp.append(it[i])
    result.append(temp)

# Sorted Revision

people = [
    {'first': 'John', 'last': 'Smith', 'age': 25},
    {'first': 'Alice', 'last': 'Smith', 'age': 30},
    {'first': 'Bob', 'last': 'Adams', 'age': 22},
    {'first': 'Charlie', 'last': 'Adams', 'age': 28},
    {'first': 'David', 'last': 'Brown', 'age': 25}
]

def sort_people(people_list):
        return sorted(people_list, key = lambda person:(person['last'], person['first']))


# 2

numbers = [
    [10, 20, 30],
    [5, 5, 5, 5],
    [100, 1],
    [7, 8, 9],
    [2, 3]
]

def sort_numbers(num_list):
    return sorted(num_list, key = lambda list_item : (sum(list_item)) )


print(sort_numbers(numbers))