import random
import string


def create_password_generator(characters):
    def create_password(length):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)

    return create_password

# alpha_password = create_password_generator('1234567')
# symbol_password = create_password_generator('!@#$%')
#
# print(alpha_password(5))
# print(alpha_password(10))
# print(symbol_password(5))
# print(symbol_password(10))


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):

   def check_password(password):
       upper, lower, punct, digits = [0,0,0,0]

       for char in password:

           if char.islower():
               lower += 1
           if char.isupper():
               upper += 1
           if char.isdigit():
               digits += 1
           if char in string.punctuation:
               punct += 1

       if upper < min_uppercase or lower < min_lowercase or punct < min_punctuation or digits < min_digits:

           return False
       return True

   return check_password


# check = create_password_checker(1,1,1,1)
# print(check("Hello.2020"))


def getitem(somearg):

    def f(someiterab):
        if somearg in someiterab:
            return someiterab[somearg]
        else: return 'Not Found'

    return f

#
# ff = getitem('c')
#
# print(ff({'a' : 1, 'b' : 2, 'c' : 0}))


def doboth(f1, f2):
    '''g(x) = f2(f1(x))'''
    def g(x):
        somevar = f1(x)
        somevar = f2(somevar)
        return somevar


    return g

def f1(x):
    return x**2
def f2(x):
    return x+3

f = doboth(f1,f2)
print(f(2))