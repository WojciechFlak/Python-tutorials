import datetime as dt
import sys


class MillionDays:

    def __init__(self, day, month, year, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    "To avoid infinite range of steps in iteration there is a limitation."
    "Object has to be iterable to pass though the for loop."
    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()  # stops iteration in for loop
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    "This method provides the ability to generate next iterations of itself."
    def __iter__(self):
        return self


start = dt.datetime.now()

md = MillionDays(1, 1, 2000, 35)


print(next(md))
print("--")
print(next(md))
print("--")

for i in md:
    print(i)


stop = dt.datetime.now()
exec_time = stop - start
print(exec_time)

print(sys.getsizeof(md))
