import operator

PEOPLE = [{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il','age':39},
{'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov', 'age':80 },
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru', 'age':70}
]



def alf(list_of_dicts):
    return sorted(list_of_dicts, key = lambda x : (x['last'], x['first']))

def alphabetize(list_of_dicts):
    return sorted(list_of_dicts, key = operator.itemgetter('age','first'))



# def alphabetize_name(const):
#     newPeople = []
#     temp_lnames = []
#     temp_fnames = []
#     for dicts in const:
#
#         temp_lnames.append(dicts['last'])
#         temp_fnames.append(dicts['first'])
#     sorted(temp_lnames)
#     sorted(temp_fnames)
#
#     print(temp_fnames)
#     print(temp_lnames)
#
# def alphabetize(list_of_dicts):
#     return sorted(list_of_dicts, key = operator.itemgetter('last', 'first'))
#
# alphabetize_name(PEOPLE)
#

numbers = [-15, 8, -3, 12, -7, 0, 4, -20, 11, -1, 6, -9, 14, -2, 5]

absolute = sorted([abs(x) for x in numbers])


words = [
    "apple",
    "banana",
    "cherry",
    "dog",
    "elephant",
    "forest",
    "guitar",
    "house",
    "island",
    "jacket",
    "keyboard",
    "mountain",
    "notebook",
    "orange",
    "python"
]

vowels = set('aeiou')

def vowel_counter(listt):
    word_dict = {}
    for word in listt:
        counter = 0
        for letter in word:
            if letter in vowels:
                counter+=1
        word_dict.update({word: counter})
    return word_dict


word_dict = vowel_counter(words)

def sort_by_vowel(mydict):
     mydict = dict(sorted(mydict.items(), key = lambda item:(item[1], item[0] )))
     return list(mydict.keys())

words2 = sort_by_vowel(vowel_counter(words))


sorted_words = sorted(words, key = lambda word: (sum(letter in vowels for letter in word), word))

numbers : list[list[int]] = [
    [3, 7, 2],
    [10, 5],
    [],
    [1, 2, 3, 4],
    [20],
    [4, 4, 4],
    [8, 1],
    [2, 2, 2, 2, 2],
    [15, 3]
]



sorted_nums = sorted(numbers, key=lambda num_sum: int(sum(num_sum)))
print(sorted_nums)