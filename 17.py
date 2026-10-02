import ipaddress
import os
import re
from os.path import splitext

numbers = [1, 2, 3, 1, 2, 3, 4, 1]

def  how_many_different_numbers(some_list):
    return len(set(some_list))

# bad
def get_unique_ip(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().split()
        ip_list = []
        for i in range(0, len(words), 10):

            ip_list.append(words[i])
        ip_list= set(ip_list)
    return ip_list

def get_unique_ip2(filename):
    ips = set()
    with open(filename, 'r', encoding='utf-8', errors='replace') as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            try:
                ips.add(str(ipaddress.ip_address(parts[0])))
            except ValueError:
                continue
    return ips

#print(get_unique_ip2('logs.txt'))

def get_server_response(filename):
    responses = set()
    status_re = re.compile(r'"\s+([1-5]\d{2})\s')   # status code after request line
    with open(filename, 'r', encoding='utf-8', errors='replace') as file:
        for line in file:
            m = status_re.search(line)
            if m:
                responses.add(m.group(1))
    return responses

# get file suffix

files = os.listdir()
extensions = set()
for i in files:
    separated = splitext(i)
    extensions.add(separated[1])
print(extensions)