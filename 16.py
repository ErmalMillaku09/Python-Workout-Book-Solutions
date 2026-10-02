from random import random

dict1 = {'a':2, 'b':1}


def dict_diff(dict1, dict2):
    output = {}

    all_keys = dict1.keys() | dict2.keys()

    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            output[key] = {dict1.get(key), dict2.get(key)}
    return output

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4, 'd':4}

# print(dict_diff(d1, d2))

def dict_merge(*dicts):
    output = {}

    for dictionary in dicts:
        for key in dictionary.keys():
            output[key] = dictionary[key]
    return output

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4, 'd':4}
d3 = {'a':1, 'b':2, 'c':4, 'd':5, 'e':6}
# print(dict_merge(d1,d2, d3))




even_arguments = ['a', 1, 'b', 2, 'c', 3, 'd', 4]
if len(even_arguments) % 2 != 0:
    even_arguments.pop()

def dict_even(*args):
    output = {}
    for i in range(0, len(args),2):

        output[args[i]] = args[i+1]

    return output

#print(dict_even(*even_arguments))

def my_func(key, value):
    if key.lower() in 'aeiou' and value >2:
        return True
    else: return False





def dict_partition(dict, some_func):
    d1 = {}
    d2 = {}
    output = []
    for key, value in dict.items():
        if some_func(key, value):
            d1[key] = value
        else: d2[key] = value

    return d1, d2

d3 = {'a':1, 'b':2, 'c':4, 'd':5, 'e':6, 'f': 7}
d1v, d2c = dict_partition(d3, my_func)






