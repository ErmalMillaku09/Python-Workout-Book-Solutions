numbers = [3, 7, 10, 12, 15, 20]

list1 = [x for x in numbers if x >10]

numbers = [1, 2, 3, 4,5]

list2 = [(x, x**2) for x in numbers]

list3 = tuple(x*10 for x in numbers)


list1 = ["a", "b", "c"]
list2 = [10, 20, 30]
list3 = ["X", "Y", "Z"]

newlist = [(list1[i], list2[i], list3[i]) for i in range(len(list1))]
print(newlist)

lists = (
    ["a", "b", "c"],
    [10, 20, 30],
    ["X", "Y", "Z"]
)

result = [tuple(it[i] for it in lists) for i in range(len(lists[0]))]
# print(result)

# exercise 9

result = [tuple(current_list[i] for current_list in lists) for i in range(len(lists[0]))]
# exercise 10
# i = 0 -> go into the lists list enter the first list get index 0, then second list get index 0, then again for the third,
# in between those they are placed into a tuple. We exhaust our lists and go into outer loop
# i = 1 -> do the same but now we get the second member
# i = 2 we are on the last members of the list and iterate through them

# Bonus


# 1 , 10 , 100, 1000 -> i=0, 2, 20, 200, 2000 -> i=1, 3, 30, 300, 3000 -> i=2,
#it will run fine since the inner loop goes through the iterables and we need the outer index i only to go through each lists' members