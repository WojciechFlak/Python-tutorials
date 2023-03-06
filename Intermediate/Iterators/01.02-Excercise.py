"""
import time
import sys

products = ["Product {}".format(i) for i in range(1, 500)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 500)]
print(customers)

combinations = []

for i in products:
    for j in promotions:
        for k in customers:
            combinations.append("{} - {} - {}".format(i, j, k))

print(sys.getsizeof(combinations))

for c in combinations:
    # here an analysis will be done - currently, just nothing happens :)
    pass

time.sleep(10)
"""
import sys


class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):

        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()

        item_to_return = "{} - {} - {}"\
            .format(self.products[self.current_product],
                    self.promotions[self.current_promotion],
                    self.customers[self.current_customer])

        self.current_customer += 1

        return item_to_return

    def __iter__(self):
        return self


products = ["Product {}".format(i) for i in range(1, 3)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 3)]

combinations = Combinations(products, promotions, customers)

print(sys.getsizeof(combinations))

for i in range(60):
    print(next(combinations))
for c in combinations:
    pass
