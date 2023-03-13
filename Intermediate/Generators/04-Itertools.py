import itertools as it
import math


notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
time = 4


for permutation in it.permutations(notes, time):
    print(permutation)

print(math.factorial(len(notes))/math.factorial(len(notes) - 4))

number = 0
for permutation in it.permutations(notes, time):
    number+=1
print(number)
