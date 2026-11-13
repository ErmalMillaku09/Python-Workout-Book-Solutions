import csv

def reverse_file(path1, path2):
    with open(path1, 'r') as infile, open(path2, 'w') as outfile:
        for record in infile:
            outfile.write(f'{record.rstrip()[::-1]}\n')
            # newline = record.rstrip()
            # reversed_line = newline[::-1]
            # outfile.write(reversed_line)
            # outfile.write('\n')



# reverse_file('./etc/text1.txt', './etc/text2.txt')

def pseudo_enc(file1, file2):
    with open(file1, 'r') as infile, open(file2, 'w') as outfile:
        for record in infile:
            for char in record:
                if char == '\n':
                    outfile.write(char)
                    continue
                outfile.write(f'{str(ord(char))} ')


def pseudo_dec(file1, file2):
    with open(file1, 'r') as infile, open(file2, 'w') as outfile:
        for record in infile:
            one_line = record.split()

            for char in one_line:
                outfile.write(f'{chr(int(char))}')

            outfile.write('\n')



# pseudo_enc('./etc/text1.txt', './etc/text2.txt')
#
# pseudo_dec('./etc/text2.txt', './etc/text3.txt')


def get_letters(file1, file2, file3):
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')

    with open(file1, 'r') as infile, open(file2, 'w') as outfile1, open(file3, 'w') as outfile2:
        for record in infile:
            for char in record:
                if char == '\n':
                    outfile1.write('\n')
                    outfile2.write('\n')
                elif char in vowels:
                    outfile1.write(char)
                elif char in consonants:
                    outfile2.write(char)


# get_letters('./etc/sample.txt', './etc/vowels.txt', './etc/consonants.txt' )

def get_shells(file1, file2):
    shells = {}
    with open(file1, 'r') as infile, open(file2, 'w') as outfile:
        reader = csv.reader(infile, delimiter = ':' )
        for record in reader:
            if len(record)<2:
                continue
            shells.setdefault(record[-1],[])
            shells[record[-1]].append(record[0])

        for k, v in shells.items():
            outfile.write(f'{k}: {v}\n')
        return


get_shells('./etc/psswd.txt', './etc/shells.txt')



