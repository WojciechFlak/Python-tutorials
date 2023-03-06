import datetime as dt

class MilionDays:

    '''
    __getitem__ allows to use a particular instance. __next__ allows to iterate with next across class.
    Artificial iterator it below allows to iterate across this class in case there is no __next__ defined.
    For loop doesn't rise exception in case of the end. For __getitem__ method we should use try-except.
    '''

    def __init__(self, day, month, year, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()  # stops iteration in for loop
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret


md = MilionDays(1, 1, 2000, 300)

print(md[60])

it = iter(md)

print(next(it))
print(next(it))

print(next(md))
print(next(md))
