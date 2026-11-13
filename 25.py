def myxml(*args, **kwargs):
    if len(args) == 1:
        output = f'<{args[0]}></{args[0]}>'
    elif len(args) == 2:
        output = f'<{args[0]}>{args[0]}</{args[0]}>'
    if kwargs:
        attributes = []
        for k, v in kwargs.items():
            attributes.append(f'{k} = "{v}"')

        output = f'<{args[0]} {" ".join(attributes)}>{args[0]}</{args[0]}>'
    print(output)
# myxml('foo', 'bar', a=1, b=2, c=3)


def myxml2(*args, **kwargs):
    tag = args[0]

    content = args[1] if len(args) > 1 else ''
    attributes = ' '.join(f'{k} = "{v}"'for k,v in kwargs.items())
    return f'<{tag} {attributes}>{content}</{tag}>'

#
# print(myxml('foo', 'bar', a=1, b=2, c=3))

def copyfile (filename, *args):
    with open(filename, 'r') as infile:
        data = infile.read()
        for file in args:
            with open(file, 'w') as outfile:
                outfile.write(data)

# copyfile('./etc/vowels.txt', './etc/text1.txt', './etc/text2.txt', './etc/text3.txt')

def factorial(*args):
    result = 1
    for i in args:
        result = result * i
    return result


def anyjoin(input, glue = ' '):
     result = ""
     for char in input:
         result += char + glue

     result = result[:-2]
     return result

print(anyjoin('abc', '**'))

# print(factorial(2,3,4,5))