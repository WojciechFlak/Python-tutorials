import itertools as it

def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

# print(get_factors(20))

list_candidate = [i for i in range(10001)]

filtered_list = list(it.filterfalse(lambda x: x != sum(get_factors(x)), list_candidate))

for p in filtered_list:
    print(p)
