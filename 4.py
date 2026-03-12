def hex_output(num):
    """Hex to decimal converter"""
    total = 0
    pow = 0
    while num > 1:
        iterator = num % 10
        num = int(num / 10)
        total += iterator * (16**pow)
        pow += 1
    return total

# t = hex_output(610)
# print(t)


def hex_output2(num):
    """Hex to decimal converter"""
    pow = 0
    total = 0
    num = reversed(num.upper())
    for index, digit in enumerate(num):
        try:
            digit = int(digit)
            total += digit * (16**pow)
            pow +=1
        except (ValueError, TypeError):
            match digit:
                case "A":
                    digit = 10
                case "B":
                    digit = 11
                case "C":
                    digit = 12
                case "D":
                    digit = 13
                case "E":
                    digit = 14
                case "F":
                    digit = 15
                case "_":
                    print("Please enter a valid hex number")
                    return

            total += digit * (16 ** pow)
            pow += 1

    return total
# Enumerate returns a tuple on each iteration of an index, and the iterable element index, item_at_index

def hex_output3(num):
    total = 0
    power = 0
    num = reversed(num.upper())

    for digit in num:
        try:
            value = int(digit)
        except ValueError:
            hex_map={
                "A":10, "B":11, "C":12, "D":13, "E":14, "F":15,
            }
            if digit not in hex_map:
                raise ValueError("Please enter a valid hex number")
            value = hex_map[digit]
        total += value * (16 ** power)
        power += 1

    return total




# ord and chr functions (Unicode mapping characters or ints visa vi)
# ord() takes in a character and returns its unicode value for example A = 65
# chr takes in an int and returns the character

def hex_output4(num):
    total = 0
    power = 0
    num = reversed(num.upper())
    for digit in num:
        try: value = int(digit)
        except ValueError:
            if ord(digit) in range(65,71):
                value = ord(digit) - 55
            else: raise ValueError("Please enter a valid hex number")
        total += value * (16 ** power)
        power +=1
    return total




def hex_output5(num):
    total = 0
    for digit in num.upper():
        try:
            value = int(digit)
        except ValueError:
            if 'A' <= digit <= 'F':
                value = ord(digit) - 55
            else:
                raise ValueError("Invalid hex digit")

        total = total * 16 + value

    return total


p = hex_output5("1F")
print(p)