import operator
from functools import reduce


# def foo(x):
#     def bar(y):
#         return x*y
#     return bar
#
#
# f = foo(10)
# print(f(20))

# Remember LEGB for scope defintion in python, this one just makes f like a pointer for bar which is defined only when foo is called first



def calc(operation):

    operations  = {
        '+': operator.add ,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }

    operand_num = operation.split()
    operator_symbol = operand_num[0]


    num1, num2 = int(operand_num[1]), int(operand_num[2])

    opr = operations[operator_symbol]

    return opr(num1,num2)


def calc2(operation):

    operations  = {
        '+': operator.add ,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }

    operand_num = operation.split()
    operator_symbol = operand_num[0]

    numbers = [int(x) for x in operand_num[1:]]


    opr = operations[operator_symbol]

    return reduce(opr, numbers )

def square(x):
    return x ** 2


def apply_to_each(funct, iterab):
    new_iterab = []

    for i in iterab:
        new_iterab.append(funct(i))

    return new_iterab


# print(apply_to_each(square, (1,2,3,4)))

def transform_lines(funct, inputfile, outputfile):
    with open(inputfile, 'r') as infile, open(outputfile, 'w') as outfile:
        for line in infile:
            outfile.write(funct(line,3))



def caesar_cipher(charlist, key):
    encrypted = ''
    punctuation = ' .,?!'
    for char in charlist.lower():

        if char not in punctuation and ord(char) != 10:
            encrypted +=chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted


transform_lines(caesar_cipher, './etc/plain.txt', './etc/enc.txt')

