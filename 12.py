from collections import Counter

# str = "hello"
#
# def most_repeating_word(wordlist):
#     # for each word add it and its most common letter to the dictionary  hello, (l,2)
#     word_letter = {}
#     for i in wordlist:
#         word_letter.update({i: word_letter_getter(i) })
#
#     word, most_reps = max(word_letter.items(), key = lambda kv :kv[1][1])
#     return (word, most_reps)
#
# def word_letter_getter(word):
#     word_dict = {}
#
#     for i in range(len(word)):
#         if word[i] in word_dict:
#             continue
#         count = 1
#
#         for j in range(i + 1, len(word)):
#             if word[j] == word[i]:
#                 count += 1
#
#         word_dict[word[i]] = count
#
#     letter, repetitions = max(word_dict.items(), key=lambda kv: kv[1]) #kv[1] gives the key to filter by the
#     # second value
#     return (letter, repetitions)
#
#
# words = ['this','is', 'an', 'elementary','test', 'example']
#


### book solution
WORDS = ['this', 'is', 'an','elementary', 'test', 'example']

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(wordlist):
    return max(wordlist, key = most_repeating_letter_count)


print(most_repeating_word(WORDS))