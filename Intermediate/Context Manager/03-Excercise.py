# Error handling in exit method: when return False it hides the error, when True - prints it out.


import os
import requests
import zipfile


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError:
            print(exc_val)
            return True
        elif exc_type == KeyError:
            print(exc_val)
            return True
        else:
            return False


path = '../Context Manager/tmp_file.zip'
url_path = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'

with FileFromWeb(url_path, path) as file:
    with zipfile.ZipFile(file.file, 'r') as zip:
        a_file = zip.namelist()[0]
        print(a_file)
        os.chdir('../Context Manager')
        zip.extract(a_file, '.', None)
