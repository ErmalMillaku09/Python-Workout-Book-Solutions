def mysum(mylist):
    """List as an argument"""
    c= 0
    for i in mylist:
        c += mylist[i]
    return c


# mylist = (0,1,2,3)
#
# n = mysum(mylist)
#
# print(n)

# If we get an iterable as the argument
# *args unpacks elements in an iterable object
# **kwargs unpacks them in the same manner but for a key value

def mysum2(*iterab):
    """Iterable as an argument any number of arguments"""
    sum = 0
    for number in iterab:
        sum += number
    return sum
# print(mysum2(1,2,3))
# Adding a second argument for a starting variable to be added



def mysum3(list, sp = 0):
    """Iterable as an argument with a start point"""
    sum = sp
    for number in list:
        sum += number
    return sum

def mysum4(*numbers):
        """Many arguments with average"""
        sum = 0
        for number in numbers:
            sum += number
        return sum/len(numbers)

## print(mysum4(1,2,3))

## Take a list of words, return longest, shortest, average word length
def mysum5(strlist):
    shortest = 100
    longest = 0
    avg = 0
    for str in strlist:
        if (len(str)<shortest):
            shortest = len(str)
        if (len(str)>longest):
            longest = len(str)
        avg += mysum2(len(str))

    avg = avg/len(strlist)
    # Returning like this python autopacks them into a tuple
    return shortest,longest, avg

# wordlist = ['dog','cat','rat','hatter']
# print(mysum5(wordlist))

## Take a list of object try to turn them into int

def mysum6(objlist):
    total = 0
    for obj in objlist:
        try:
            total += int(obj)
        except(ValueError, TypeError):
            pass
    return total


##