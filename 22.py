import csv
import json
import glob
import os
import arrow

def print_scores(dirname):
    scores = {}
    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}
        with open(filename, 'r') as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:

        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) / (len(subject_scores)))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')




def csv_to_json(filepath, newfile):

    main_list = []
    with open(filepath,'r') as passwd:
        infile =  csv.reader(passwd, delimiter=':')
        for record in infile:
            main_list.append(tuple(record))

    with open(newfile, 'w') as output:
        json.dump(main_list, output)
# csv_to_json('./etc/psswd.txt', './etc/newtxt.json')


def csv_to_json2(filepath, newfile):
    with open(filepath, 'r') as passwd, open(newfile, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        output.write('[')
        first_record = True
        for record in infile:
            if not first_record:
                output.write(',')

            output.write(json.dumps(record))
            first_record = False

        output.write(']')

# csv_to_json2('./etc/psswd.txt', './etc/newtxt.json')

def csv_to_dict(filepath):
    fieldnames = ['username', 'password', 'uid', 'gid',
              'description', 'home', 'shell']
    dict_list = []
    with open(filepath, 'r') as infile:
        for row in  csv.DictReader(infile, fieldnames, delimiter=':'):
            temp_dict = {}
            for field in fieldnames:
                temp_dict[field] = row[field]
            dict_list.append(temp_dict)
        infile.close()
    return dict_list

# listt = csv_to_dict('./etc/psswd.txt')

def csv_to_dict2(filepath):
    fieldnames = ['username', 'password', 'uid', 'gid',
              'description', 'home', 'shell']
    dict_list = []
    with open(filepath, 'r') as infile:
        dict_list = list(csv.DictReader(infile, fieldnames, delimiter=':')) # dict reader reads the entire file
    return dict_list

# listt2 = csv_to_dict('./etc/psswd.txt')
# print(listt2)



# enter dir, get file data, skip sub dirs. get size and date modified.

def get_file_stats():
    dirpath = './etc' #input("Enter Directory path: ")
    try:
        files = os.listdir(dirpath)
    except FileNotFoundError:
        print("Not a valid path")
        return

    temp_list = []

    for file in files:
        file_dict = {}
        modified_time, size =(lambda s:(s.st_mtime, s.st_size)) (os.stat(os.path.join(dirpath,file)))

        file_dict["filename"]= file
        file_dict["size"] = size
        file_dict["date-modified"] = modified_time
        temp_list.append(file_dict)

    with open('./etc/file-info.json', 'w') as outfile:
        json.dump(temp_list, outfile, indent = 4)

    with open('./etc/file-info.json', 'r') as f:
        data = json.load(f)
        file_list = sorted(((file["filename"], file["date-modified"]) for file in data), key = lambda x: x[1], reverse= True)
        file_list_by_size = sorted(((file["filename"], file["size"]) for file in data), key = lambda x: x[1], reverse= True)

        print(f"Most recently modified files: {file_list}")
        print(f"Files ordered by size: {file_list_by_size}")





# [{"name": "filename", "size": size, "date-modified": }]

print(get_file_stats())

