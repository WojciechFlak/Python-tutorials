import os


def gen_get_files(dir, file_extention):
    for dir_name, subdir_name, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith(file_extention):
                full_path = os.path.join(dir_name, filename)
                yield full_path


def grep(filename, search_string):
    for file in filename:
        with open(file) as line:
            if search_string in line.read():
                yield file


path = '../../Intermediate/Iterators'
file_extension: str = '.py'
search_string: str = 'os'


generated_files = gen_get_files(path, file_extension)

for i in grep(generated_files, search_string):
    print(i)
