import math
from functools import total_ordering


def run_timing():

    run_list=[]
    while True:
        time = input("Enter your run time in minutes: ")
        if time == '':
            break
        try:
            time = int(time)
            run_list.append(time)
        except (ValueError,TypeError):
            print("Please enter a number")
            continue
    avg_run = sum(run_list)/(len(run_list))

    print(f"Average run time {avg_run}")

def run_timing2():

    total = 0
    num_runs = 0
    while True:
        one_run = input("Enter your run time in minutes: ")
        if not one_run:
            break
        try:
            one_run = int(one_run)
            total += one_run
            num_runs += 1
        except (ValueError,TypeError):
            print("Please enter a number")
            continue
    avg_run = total/num_runs

    print(f"Average run time {avg_run}")


# 3.1
# 123,456, 2 , 3 -> 23,456
def truncate_nums(decim_num, before, after):
    """Get a float number and truncate it to the amount specified by the two int 123,45, 2, 1 -> 23,4
    -> two numbers on decimal and 1 after decimal point"""
    integer_part, decimal_part = str(decim_num).split(".")
    integer_part = integer_part[-before:]
    decimal_part = decimal_part[:after]

    print(float(integer_part + "." + decimal_part))
# [:after] -> Slice index from 0 (since its ommited) to after
# [-before:] start from the end minus - before to the end.( Start from the right)
def truncate_number(num, before, after):
    integer = int(num)
    decimal = num - integer

    integer_part = integer % (10 ** before)

    decimal_part = math.floor(decimal * (10 ** after)) / (10 ** after)

    return integer_part + decimal_part

t =truncate_number(123.456, 1, 2)

print(t)