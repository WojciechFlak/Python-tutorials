from contextlib import contextmanager, redirect_stdout


class Door:

    def __init__(self, room):
        self.room = room

    def open(self):
        print("Opening the door to: {}".format(self.room))

    def close(self):
        print("Closing the door to: {}".format(self.room))


# d = Door('kitchen')
# d.open()
# d.close()

@contextmanager
def open_and_close(func):
    func.open()
    yield func
    func.close()


# with open_and_close(Door('bedroom')) as bedroom:
#     print("Entering the room.")

r = open('../Context Manager/04.02-output.txt', 'a+')
with redirect_stdout(r):
    print("Hello World!")

    with open_and_close(Door('bedroom')) as bedroom:
        print("Entering the room.")
