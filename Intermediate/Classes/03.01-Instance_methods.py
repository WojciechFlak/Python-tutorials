class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print('{}'.format(self.name.upper()))
        print('Kind:    {}'.format(self.kind))
        print('Taste:   {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print('\t', a)
        if len(self.filling) > 0:
            print('Filling:  {}'.format(self.filling))
        print('--'*10)

    def set_fillling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


baker_offer = []
cake01 = Cake('Vanilla cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolate', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

baker_offer.append(cake01)
baker_offer.append(cake02)
baker_offer.append(cake03)

print('Today in the offer:')
for c in baker_offer:
    c.show_info()

cake03.set_fillling('peanut')
cake03.add_additives(['powder'])
cake03.show_info()
