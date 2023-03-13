import os
import requests


def get_files(dir):
    for d in os.listdir(dir):
        yield os.path.join(dir, d)


def get_lines(filename):
        with open(filename, 'r') as f:
            for l in f.readlines():
                yield l.replace('\n', '')


def check_webpage(url):

    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False



try:
    os.mkdir('../Generators/files')
except:
    pass

with open('../Generators/files/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('../Generators/files/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')



path = '../Generators/files'

for f in get_files(path):
    for l in get_lines(f):
        print(f, l, check_webpage(l))
