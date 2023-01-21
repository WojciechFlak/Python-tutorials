# else - while there was no error
# finally - at the end no matter what
# except Exception as e:

# import requests
# import os
# import shutil
# import  sys
#
# import urllib3.connection
#
#
# def save_url_to_file(url, file_path):
#     r = requests.get(url, stream=False)
#     with open(file_path, "wb") as f:
#         f.write(r.content)
#
#
# url = 'http://www.mobilo24.eu/spis/'
# dir = '/Users/wojciechflak/PycharmProjects/Nauka/TRY-files'
# tmpfile = 'download.tmp'
# file = 'spis.html'
#
# tmpfile_path = os.path.join(dir, tmpfile)
# file_path = os.path.join(dir, file)
#
#
# try:
#     if os.path.exists(dir) is False:
#         os.makedirs(dir)
#     if os.path.exists(tmpfile_path):
#         os.remove(tmpfile_path)
#     save_url_to_file(url, tmpfile_path)
#     shutil.copy(tmpfile_path, file_path)
# except requests.exceptions.ConnectionError as e:
#     print('URL is not valid')
# except FileNotFoundError as e:
#     print('Sth wrong with file access.')
# except TypeError as e:
#     print('Open function should be switched to write bytes.')
# except Exception as e:
#     print(e)
#     print(sys.exc_info()[0])
# else:
#     print('Done')
# finally:
#     if os.path.exists(tmpfile_path):
#         os.remove(tmpfile_path)


import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, list_of_trips):
        list_of_errors = []
        for trip in list_of_trips:

            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append('{} : {}'.format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append('{} : {}'.format(trip.symbol, str(e)))

        if len(list_of_errors) > 0:
            raise Exception('The list of errors: {}'.format(list_of_errors))

        else:
            print('The offer will be published...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]


try:
    print('Checking the trips.')
    Trip.publish_offer(trips)
    print('Done.')
except Exception as e:
    print('error')
    print(e)