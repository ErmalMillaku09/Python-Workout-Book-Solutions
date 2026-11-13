import os
import string
import hashlib
import arrow
from collections import Counter

def wordcount(filename):

    with open(filename, 'r', encoding='utf-8') as f:
        lines = 0
        words = 0
        chars = 0

        distinct_words = set()
        for line in f:
            lines +=1
            chars += len(line)
            for word in line.split():
                words +=1
                distinct_words.add(word)

        print(f"Number of characters (including whitespace): {chars}")
        print(f"Number of words (separated by whitespace): {words}")
        print(f"Number of lines: {lines}")
        print(f"Number of unique words (case sensitive): {len(distinct_words)}")

def wordcount2(filename):
    count ={'lines':0, 'words':0, 'chars':0}
    unique_words = set()

    with open(filename, 'r') as f:
        for one_line in f:
            count['lines'] +=1
            count['words'] +=len(one_line.split())
            count['chars'] +=len(one_line)

            unique_words.update(one_line.split())
    count['unique words'] =  len(unique_words)
    for k,v in count.items():
        print(f"{k} : {v}")



# wordcount2('scratch.txt')

def get_word_frequency():
    filename = input("Enter a filename you want to analyze: ")
    filename = filename.strip() + '.txt'
    words = input("Enter words you want to get frequency off(Separate them with space): ")
    words = words.split()

    word_dict = {word : 0 for word in words}

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                if word in word_dict.keys():
                    word_dict[word] +=1


    return word_dict



def get_file_size(dir = '.'):
    files_size = {}
    files = os.listdir(dir)
    for i in files:
        files_size[i] = os.stat(i)[6]

    return files_size

# dd = get_file_size()
# for k, v in dd.items():
#     print(f"{k} : {v}")


def get_letter_freq_dir(dir = '.'):
    alpha_dict = {ch :0 for ch in string.ascii_lowercase}
    files = os.listdir(dir)
    filtered = [file for file in files if file.lower().endswith('.txt')]

    for file in filtered:
        new_path = os.path.join(dir, file)
        with open(new_path, 'r', encoding='utf-8') as current:
            for char in current.read():
                if char.isalpha():
                    if char.lower() in alpha_dict:
                        alpha_dict[char.lower()] += 1
    return alpha_dict

# dd = get_letter_freq_dir('./etc')
# top_five = sorted(dd.items(), key = lambda item: item[1], reverse=True)[:5]
# for k,v in dd.items():
#
#     print(f"{k} : {v}")
# print(top_five)





def find_longest_word(filename):
    """find_longest_word takes a filename as an
    argument and returns the longest word found in the file."""

    with open(filename, 'r', encoding='utf-8') as f:
        longest_word = max(f.read().split(), key = len)

    return longest_word

def find_all_longest_words(directory = ''):

    """The second function, find_all_longest_words, takes a directory name and returns a dict in which the keys are
    filenames and the values are the longest words from each file"""
    files_dict = {}
    filtered = [file for file in os.listdir(directory) if file.lower().endswith('.txt')]
    for file in filtered:
        new_path = os.path.join(directory, file)
        files_dict[file] = find_longest_word(new_path)

    return files_dict


# dd = find_all_longest_words('./etc')
#
# for k,v in dd.items() :
#     print(f"{k} : {v}")



def hash_dict(directory):
    files = os.listdir(directory)
    hd = {}
    for file in files:
        with open(os.path.join(directory, file), 'rb') as f:
            hash = hashlib.md5(f.read())
        hd[file] = hash.hexdigest()

    return hd

# dd = hash_dict('./etc')
#
# for k,v in dd.items():
#     print(f"{k} : {v}")


def show_tree(directory):
    utc = arrow.utcnow().shift(hours=+2)

    files = os.listdir(directory)
    for file in files:
        mtime =arrow.get(os.stat(os.path.join(directory,file)).st_mtime)
        print(f"{file} was modified at: {mtime.humanize()}")

show_tree('./etc')

def summarize_requests(filename):
    responses = Counter()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            responses[line.split()[8]] +=1
    return responses

#dd = summarize_requests('./etc/mini-access-log.txt')

