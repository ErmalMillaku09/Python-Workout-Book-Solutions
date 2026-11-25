import random
def join_numbers(x):
    return ','.join([str(z) for z in range(x)])

# x = join_numbers(15)
# print(x)
#
#
#
# numbers = range(10)
#
# print([(x,y)
#        for x in numbers
#        if x % 2 == 0
#        for y in numbers
#        if y % 3 == 0
# ])

all_places = {'USA': ['Philadelphia', 'New York', 'Cleveland', 'San Jose',
'San Francisco'],
'China': ['Beijing', 'Shanghai', 'Guangzhou'],
'UK': ['London'],
'India': ['Hyderabad']}

# cities = [one_city
#           for country, cities in all_places.items()
#           for one_city in cities]

city_country = [(one_city, one_country)
                for one_country, all_cities in sorted(all_places.items())
                for one_city in sorted(all_cities)
]

numbers2 = [int(random.random()*90) for x in range(10)]
# print(numbers2)
def join_numbers_2(x):
    return [num for num in x if 10 > num >= 0]


def sum_hexes(z):
    return sum(int(x, 16) for x in z)


nums3 = ['0x16', '0xFF', '0xAE']
#
# print(sum_hexes(nums3))


def reverse_word_order(filepath, filepath2):
    with open(filepath, 'r') as infile, open(filepath2, 'w') as outfile:
        for record in infile:
            line = record.split()
            print(line)
            outfile.write(' '.join(line[::-1])+'\n')


reverse_word_order('./etc/sample.txt', './etc/sample2.txt')
