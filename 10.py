from unittest import skip


def mysum(*args):

    if not args:
        return args
    result = args[0]
    for item in args[1:]:
        result+= item
    return result



def mysum_bigger_than(baseline, *args):
    if not baseline:
        baseline = -99999999999

    for item in range(len(args)):
        if args[item]>baseline:
            result = args[item]
            index = item

            break
    print(index)
    for item in range(index+1, len(args)):

        if args[item] > baseline:
            result += args[item]
    return result

# def mysum_bigger_than(baseline, *args):
#     return sum(item for item in args if item > baseline)


def mysum_bigger_than2(baseline, *args):
    result = None

    for item in args:
        if item > baseline:
            if result is None:
                result = item
            else: result += item
    return result



#print(mysum_bigger_than2(10, 5, 20, 30, 6))


def sum_numeric(*args):
    result = 0
    for item in args:
        print(item)
        try:
            result += int(item)
        except:
            continue
    return result

def sum_numeric2(*args):
    return sum(int(item) for item in args if str(item).lstrip("-").isdigit())

# print(sum_numeric2(10, 20, 'a', '30','bcd'))


data = [
    {'a': 1, 'b': 2,'c':3},
    {'a': 10, 'c': 3},
]

result = {}
# for i in data:
#     for key in i:
#         result.update({key: i[key]})
#


def dictionaries_to_dictinoary(dict):
    for i in data:
        for key in i:
            if key in result.keys():
              result[key] = [result[key], i[key]]
            else:
                result[key] = i[key]



print(result)
