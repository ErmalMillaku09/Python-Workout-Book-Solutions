#when you use a slice, you’re guaranteed to get the same type back
# Return first and last of each type in same type
def firstlast(iterable):
    return iterable[:1] + iterable[-1:]

str ='abcd'

def even_odd_sums(iterable):
    return type(iterable)((sum(iterable[::2]), sum(iterable[1::2])))



def plus_minus(iterable):
    return iterable[0] + sum(iterable[1::2]) - sum(iterable[2::2])


## ****
def plus_minus2(iterable):
    return iterable[0] + sum(x if i % 2 == 0 else -x for i, x in enumerate(iterable[1:]))



def my_zip(listt, iterable):
    new_list = []
    for index in range(len(listt)):
       new_list.append((listt[index], iterable[index] ))

    return new_list

def my_zip2(*iterables):
#"Give me the i-th item from each iterable, and put all those items into a tuple."
    return [tuple(it[i] for it in iterables) for i in range(len(iterables[0]))]

# [WHAT_YOU_WANT for VARIABLE in SOMETHING]

print(my_zip2([10, 20,30], 'abc'))


list1 = [1,2,3]
list2 = [4,5,6]
lists = (list1, list2)

addhere = []

for i in range(len(list1)):
    temp = []
    for it in lists:
        temp.append(it[i])

    addhere.append(tuple(temp))
print(addhere)