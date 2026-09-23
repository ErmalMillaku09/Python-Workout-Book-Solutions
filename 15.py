from collections import defaultdict
import string
from operator import index


def get_rainfall():
    cities = defaultdict(lambda : [0,0]) # rainfall, days

    while True:
        city_name = input("Enter city name: ")
        if not city_name:
            break

        rainfall = input("Enter rainfall in mm: ")
        cities[city_name][0] = int(rainfall) + cities[city_name][0]
        print(cities[city_name][0])
        if city_name in cities.keys():
            cities[city_name][1] +=1

    for city, rainfall in cities.items():
        print(f'\n The city of {city} had {rainfall[0]} mm with an average of {rainfall[0]/rainfall[1]} mm per day')

#get_rainfall()

# Read logs add them to a dict based on server response

response_log = defaultdict(lambda: [0])

def logger():
    with open('logs.txt','r', encoding='utf-8') as file:
        line_list = [line.split() for line in file]
        for list in line_list:
            response_log[list[8]].append(list[0])

        for i in response_log:
            print(f'{i} : {response_log[i]}')


# Read a file and tell how many words of each length are in it

def word_length():
    word_dict = {}# length : counter
    with open('scratch.txt', 'r', encoding='utf-8') as file:
        # line_list = [word for line in file for word in line.split()]
        words = file.read().split()
        for word in words:
            word_dict[len(word)] = word_dict.get(len(word), 0 ) + 1
    for k, v in word_dict.items():
        print(f'{k}: {v} ')
word_length()