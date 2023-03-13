import random


def random_flavours_ratio(number_of_draws):

    flavours = ['sweet', 'sour', 'salty']

    for _ in range(number_of_draws):

        summ = 0
        ratio_list = []

        while summ != 1.0:
            r = round(random.random(), 2)
            ratio_list.append(r)
            if len(ratio_list) == 3:
                if sum(ratio_list) == 1.0:
                    break
                else:
                    ratio_list = []

        sample = []
        for f in range(3):
            s1 = (flavours[f], ratio_list[f])
            sample.append(s1)
        yield sample


for i in random_flavours_ratio(10):
    print(i)



'''
import random
 
 
def random_with_sum(number_of_values, asserted_sum):
 
    trial = 0
    numbers = list(range(number_of_values))
    while True:
 
        trial +=1
        for i in range(number_of_values):
            numbers[i] = random.randint(1, 101)
 
        if sum(numbers) == asserted_sum:
            yield((trial, numbers))
            trial = 0
 
 
for i in range(10):
    (number_of_trials, numbers) = next(random_with_sum(3, 100))
    print(number_of_trials, numbers)
'''
