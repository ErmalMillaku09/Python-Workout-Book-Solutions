import operator
from collections import namedtuple
from numbers import Number
from tempfile import template

PEOPLE = [('Madelline', 'Albright', 6.18),
    ('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]


def format_sort_records(somelist):
  somelist = sorted(somelist, key = lambda person:(person[1], person[0]))
  for i in somelist:
    print(f"{i[0]:<10}\t {i[1]:<10} \t {round(i[2], 2):<5}")


# format_sort_records(PEOPLE)

# Book Solution

def format_sort_records2(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples, key = operator.itemgetter(1,0)):
        output.append(template.format(*person))
    return output

Person = namedtuple('Person','Name, LName, TOA')


Person1 = Person('Madelline', 'Albright', 6.18)
Person2 = Person('Donald', 'Trump', 7.85)
Person3 = Person('Vladimir', 'Putin', 3.626)
Person4 = Person('Jinping', 'Xi', 10.603)

PersonList =[Person1, Person2, Person3, Person4]

def format_sort_records3(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples, key = lambda person: (person.LName, person.Name)):
        output.append(template.format(*person))
    return output


# for record in format_sort_records3(PersonList):
#     print(record)


#

MOVIES = [
    ('One Battle after Another', 161, 'Paul Thomas Anderson'),
    ('Bugonia', 118, 'Yorgos Lanthimos'),
    ('F1', 155, 'Joseph Kosinski'),
    ('Frankenstein', 149, 'Guillermo del Toro'),
    ('Hamnet', 125, 'Chloé Zhao'),
    ('Marty Supreme', 137, 'Josh Safdie'),
    ('The Secret Agent', 158, 'Kleber Mendonça Filho'),
    ('Sentimental Value', 133, 'Joachim Trier'),
    ('Sinners', 137, 'Ryan Coogler'),
    ('Train Dreams', 102, 'Clint Bentley'),
]



def get_input():
    print("How would you like to sort the movies?\n1. Title \n2. Length \n3. Director")
    sort_choice = input("Enter a number to sort: ")
    return int(sort_choice) -1

def format_movies(movies, sort_choice):
    output = []
    template = '{1:^4} {2:^30}  {0:^30}'
    for movie in sorted(movies, key = operator.itemgetter(sort_choice)):
        output.append(template.format(*movie))
    return output



def format_movies2(movies, sort_choices):
    sort_choices =  sort_choices.split(';')
    for i in range(len(sort_choices)):
        sort_choices[i] = int(sort_choices[i])-1

    output = []
    template = '{1:^4} {2:^30}  {0:^30}'
    for movie in sorted(movies, key = operator.itemgetter(*sort_choices)):
        output.append(template.format(*movie))
    return output

def get_input2():

    print("How would you like to sort the movies?\n1. Title \n2. Length \n3. Director")
    sort_choices = input("Enter numbers separted by ; to sort: ")
    return sort_choices

choices = get_input2()
print(f"{'Length':15} {'Director':20}  {'Name':>8}")
print('\n'.join(format_movies2(MOVIES, choices)))
