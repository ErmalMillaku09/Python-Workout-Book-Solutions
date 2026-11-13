import csv
import json
import os
from random import random
import math
import glob

def passwd_to_csv(file1, file2):
    rows = []
    with open(file1, 'r') as f1:
        for line in f1:
            if line.startswith('#'):
                continue
        line = line.split(':')

        if len(line)>2:
            rows.append([line[0], line[2]])
    with open(file2, 'w', newline='') as f2:
        o = csv.writer(f2, delimiter='\t')
        for i in rows:
            o.writerow(i)
    return file2


passwd_to_csv('./etc/psswd.txt', './etc/somecsv.csv')

def passwd_to_csv2(passwd_filename, csv_filename, indexes, delim):
    with open(passwd_filename, 'r') as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter = delim)
        outfile = csv.writer(output, delimiter = '\t')
        for record in infile:
            if len(record)>2:
                outfile.writerow((i for i in indexes))

def get_csv_input(passwd_filename, csv_filename):
    indexes = input("Enter space separated indexes: ")
    indexes = indexes.split(' ')
    indexes = [int(x) for x in indexes]
    delim = input("Enter delimeter: ")

    passwd_to_csv2(passwd_filename, csv_filename, indexes, delim)


# get_csv_input('./etc/psswd.txt', './etc/somecsv.csv')


def dict_to_csv(dic, csvpath):
    with open(csvpath, 'w',  newline = '') as output:
        outfile = csv.writer(output, delimiter='\t')
        for k,v in dic.items():
            outfile.writerow((k, v, type(v).__name__))



my_dict = {'a' : 'dog', 'b' : 2, 'c': True, 'd' : 23 }


# dict_to_csv(my_dict, './etc/somecsv.csv')


def csv_rand(csvpath):
    with open(csvpath, 'w', newline = '') as output:
        outfile = csv.writer(output, delimiter='\t')

        for i in range(10):
            outfile.writerow(math.floor(random()*100) for i in range(10))
    output.close()

    with open(csvpath, 'r') as file:
        infile = csv.reader(file, delimiter='\t')

        numbers = [int(number) for record in infile for number in record]
        total, count = sum(numbers), len(numbers)
        print(f"total is: {total}")
        print(f"With a mean of: {total/count}")



# csv_rand('./etc/somecsv.csv')

#[file for file in os.listdir('./scores') if file.endswith('.json')] or do this

#files = glob.glob('scores//*.json')



