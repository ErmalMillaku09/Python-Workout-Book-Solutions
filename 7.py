def ub_db(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = list(word)
    for index, item in enumerate(word):
        if item in vowels:
            word[index] = f"ub{item}"
    word = ''.join(word)
    print(word)


def ubi_db(word):
    output = []
    capitalize = word[0].isupper()
    word = word.lower()
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            output.append(f"ub{letter}")
        else: output.append(letter)
    if capitalize:
        output[0] = output[0].capitalize()
    output = ''.join(output)
    return output


def remove_author(author, text):
    tokenized = text.split(" ")
    for index, word in enumerate(tokenized):
        if word == author:
            tokenized.pop(index)
    text = ' '.join(tokenized)
    return text



# text = "Ermal Here Ermal Here Ermal Here Ermal Here"
#
# print(remove_author("Ermal", text))


def url_format(url):
    tokenized = list(url)
    for index, char in enumerate(tokenized):
        order = ord(char)
        if order > 128:
           char = str(hex(order)[2:])
           tokenized[index] = f"%{char}"

    return ''.join(tokenized)

# only letters and numbers 48 57, 65 - 90, 97 - 122
def url_format2(url):
    tokenized = list(url)
    for index, char in enumerate(tokenized):
        order = ord(char)
        if order not in range(48, 58) and order not in range(65, 91) and order not in range(97, 123):
           char = str(hex(order)[2:])
           tokenized[index] = f"%{char}"
    return ''.join(tokenized)


print(url_format2("malibosi"))
