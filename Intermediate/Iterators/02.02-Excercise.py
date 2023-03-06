class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item >= len(self.products)*len(self.promotions)*len(self.customers):
            raise StopIteration()
        else:
            pos_product = item // (len(self.promotions)*len(self.customers))
            item = item % (len(self.promotions)*len(self.customers))

            pos_promotion = item // len(self.customers)
            item = item % len(self.customers)

            pos_customer = item
        return "{} - {} - {}"\
            .format(self.products[pos_product], self.promotions[pos_promotion], self.customers[pos_customer])


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)


# for i in range(30):
#     print(combinations[i])

print(combinations[4])

combinations_iterator = iter(combinations)
print(next(combinations_iterator))

for c in combinations_iterator:
    print(c)
