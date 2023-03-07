class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling


baker_offer = []
cake01 = Cake('Vanilla cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolate', ['chocolade'], '')
cake03 = Cake('uper Sweet Maringue', 'meringue', 'very sweet', [], '')

baker_offer.append(cake01)
baker_offer.append(cake02)
baker_offer.append(cake03)

print('Today in the offer:')
for c in baker_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))
