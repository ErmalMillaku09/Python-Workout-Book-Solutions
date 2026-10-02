from collections import defaultdict


def passwd_to_dict(filename):
    users = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line.strip()
            if not line or line.startswith('#'):
                continue

            fields = line.split(':')

            users[fields[0]] = int(fields[2])


    return users

def same_shell(filename):
    users = defaultdict(list)

    for line in open(filename,'r', encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        fields = line.split(':')

        users[fields[-1]].append(fields[0])



    return users

# users = same_shell('etc/psswd.txt')
#
# for k,v in users.items():
#     print(f'{k}:{v}')

def get_user_input():
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if not user_input:
            break
        try:
            user_input = int(user_input)
            numbers.append(user_input)
        except:
            print("Please Enter an integer")
            continue
    return numbers

def factor_dict():
    '''keys are the factors for each number, and the values are lists contain
    ing those of the users’ integers that are multiples of those factors'''
    nums = get_user_input()
    factors = defaultdict(list)

    for i in nums:
        for j in range(1,i+1):
            if i % j ==0:
                factors[j].append(i)

    return factors


# factors = factor_dict()
# for k,v in factors.items():
#     print(f"{k}:{v}")

def nested_dicts(filename):
    main_dict =  {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            fields = line.split(':')
            main_dict[fields[0]] = {'userId': int(fields[2]), 'homeDir':fields[-2], 'shell': fields[-1]}
    return main_dict


