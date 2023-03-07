import time

class Time_measue:

    def __init__(self):
        pass

    def __enter__(self):
        self.__start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print('Execution time: {}'.format(self.__difference))

with Time_measue():
    time.sleep(3)