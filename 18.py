import string


def print_last_line(filename):
        final_line = ''
        for line in open(filename, 'r', encoding='utf-8'):
            final_line = line

        print(final_line)



def sum_ints_in_text(filename):
    sum = 0
    for line in open(filename, 'r', encoding='utf-8'):
        for word in line.split():
            cleaned = word.strip(string.punctuation) # here
            try:
                cleaned = int(cleaned)
                sum += cleaned
            except:
                pass
    return sum

# print(sum_ints_in_text('logs.txt'))

def read_two_col(filename):
    sum = 0
    for line in open(filename, 'r', encoding='utf-8'):
        if len(line)<2:
            continue
        parts = line.split()

        try:
            sum += int(parts[0]) * int(parts[1])
        except:
            continue

    return sum


def vowel_counter(filename):
    vowel_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    with open(filename, 'r', encoding='utf-8') as f:
        for char in f.read():
            char = char.lower()
            if char in 'aeiou':
                vowel_dict[char]+=1

    print(vowel_dict)



vowel_counter('etc/scratch.txt')


