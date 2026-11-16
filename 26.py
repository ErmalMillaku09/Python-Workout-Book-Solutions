import operator

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




print(calc('** 2 3'))