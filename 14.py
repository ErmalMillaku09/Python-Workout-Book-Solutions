from operator import indexOf
from datetime import datetime, timedelta
MENU = {
    "burger": 8,
    "cheeseburger": 9,
    "chicken_sandwich": 7,
    "hot_dog": 5,
    "fries": 3,
    "onion_rings": 4,
    "salad": 6,
    "pizza_slice": 4,
    "taco": 3,
    "burrito": 7,
    "nachos": 5,
    "soda": 2,
    "water": 1,
    "coffee": 3,
    "milkshake": 5,
    "ice_cream": 4,
    "cookie": 2,
    "brownie": 3,
}


def restaurant(menu):
    running_total = 0
    orders = []
    available_items = menu.keys()
    while True:
        print("Enter your order from the menu:")
        for item, price in menu.items():
            print(f"{item}, ${price}")
        order = input("\n Enter the item you want: ")
        if order not in available_items:
            print("Item not available, please choose from the menu")
            continue
        orders.append(order)
        running_total+=int(menu[order])
        print(f"Your total is: ${running_total}")
        add_to_order = input("\nWould you like anything else Y/N?: ")

        if add_to_order == 'N':
            print("Your order is:")
            print(*orders, sep = ", ")
            print(f"Your total is ${running_total}")
            break


WEATHER_DATA = {
    '14/09/26': 24, '15/09/26': 25, '16/09/26': 26, '17/09/26': 27, '18/09/26': 28, '19/09/26': 29, '20/09/26': 30, '21/09/26': 31, '22/09/26': 32,

}

def get_weather(dataset):
    available_dates = tuple(dataset.keys())

    print("\nEnter the date to get the temperature in the format: dd/mm/yyyy")
    print("\nAvailable Dates are:")
    print(*available_dates)

    user_input = input("\nEnter Date: ")

    if user_input not in available_dates:
        print("\n\n Data not available for selected date")
        return


    index = available_dates.index(user_input)

    print(f"\nThe temperature for {user_input} was "
          f"{dataset[user_input]} Celsius")

    #Previous Dates
    previous_index = index - 1

    print("\nPrevious dates:")

    while previous_index > 0:
        date = available_dates[previous_index]
        print(f"\nThe temperature for {date} was {dataset[date]} Celsius")
        previous_index -=1

    # Subsequent dates
    next_index = index + 1
    print("\nSubsequent dates:")

    while next_index != len(available_dates):
        date = available_dates[next_index]
        print(f"\nThe temperature for {date} was {dataset[date]} Celsius")
        next_index +=1

# get_weather(WEATHER_DATA)


USERS = {
    'john_doe': 'password123',
    'alice_smith': 'helloWorld!',
    'bob1995': 'pythonRocks',
    'admin': 'admin123',
    'madeline': 'testPassword',
}


def secure_login(dataset):
    while True:
        username = input("Please enter your username: ")

        if username not in dataset.keys():
            print("Wrong credentials!")
            continue

        password = input("Please enter your password: ")
        try:
            if dataset [username] != password:
                print("Wrong password!")
                continue
        except:
            continue
        print("Successfully logged in!")

# secure_login(USERS)

FAMILY = {}

def date_parser(datestr):
    parsed_date = datetime.strptime(datestr, "%d/%m/%Y")
    return parsed_date

def add_member(name, bday):

    FAMILY.update({name: date_parser(bday)})

def calculate_days_lived():
    while True:
        name = input("Enter Member Name: ")
        bday = input("Enter Member Birthday: ")

        add_member(name, bday)

        choice = input("Do you wish to add another one? (Y/N): ")
        if choice.upper() == 'N':
            break
    while True:
        chosen_member = input("Enter a members name to see how many days they have lived: ")

        days_lived = datetime.today() - FAMILY[chosen_member]
        print(days_lived)
        go_on = input("Do you wish to do another one? (Y/N): ")
        if go_on.upper() == 'N':
            break

calculate_days_lived()