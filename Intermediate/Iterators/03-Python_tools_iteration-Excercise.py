# Tuple, list and set is iterable but requires iter() function to iterate with next().
# Function 'with open file' can be self iterated as provided below.

import csv

with open('./03-file.csv', 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    # for row in csvreader:
    #     print(' | '.join(row))
    # print(next(csvreader))

    while True:
        try:
            f = next(csvreader)
            f.append('D')
            print(f)
        except StopIteration:
            break
    print("\nAll data was processed.")
