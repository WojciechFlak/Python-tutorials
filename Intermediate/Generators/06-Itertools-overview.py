import itertools as it
import operator

data = [1, 2, 3, 4, 5]

for element in it.accumulate(data, operator.mul):
    print(element)
print('----'*10)

data1 = [1, 2, 31, 4, 5, 19, 42, 45]
result = it.accumulate(data1, max)
for each in result:
    print(each)
print('----'*10)

for i in it.count(22, 3):
    print(i)
    if i > 40:
        break
print('----'*10)

months = ['Jan', 'Feb', 'Mar']
n = 0
for i in it.cycle(months):
    n+=1
    print(i)
    if n == 7:
        break
print('----'*10)

basic = [3, 4, 5]
additional = [12, 13, 14]
for i in it.chain(basic, additional):
    print(i)
print('----' * 10)

cars = ['Opel', 'Toyota', 'BMW', 'Audi']
sale = [True, False, True, True]

for i in it.compress(cars, sale):
    print(i)
print('----'*10)

nums = [1, 2, 3, 4, 5, 6, 1, 2]
for i in it.dropwhile(lambda x: x<3, nums): # opposite funct - takewhile
    print(i)
print('----'*10)

nums = [1, 2, 3, 4, 5, 6, 1, 2]
for i in it.filterfalse(lambda x: x<3, nums):
    print(i)
print('----'*10)

cars = ['Opel', 'Toyota', 'BMW', 'Audi', 'Ford', 'Ferrari']
for i in it.islice(cars, 3, 5):
    print(i)
print('----'*10)

spades = ['Hearts', 'Tiles', 'Clovers', 'Pikes']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
for i in it.product(spades,figures):
    print(i)
print('----'*10)

months = ['Jan', 'Feb', 'Mar']
cars = ['Opel', 'Toyota', 'BMW', 'Audi', 'Ford', 'Ferrari']
for i in it.zip_longest(months, cars, fillvalue='UNKNOWN'):
    print(i)
