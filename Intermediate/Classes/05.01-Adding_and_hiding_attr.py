class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, glutenfree=False):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__glutenfree = glutenfree

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
        print('Gluten free: {}'.format(self.__glutenfree))
        print('--'*10)

    def set_fillling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


baker_offer = []
cake01 = Cake('Vanilla cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolate', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True)
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')


print('Today in the offer:')
for c in Cake.bakery_offer:
    c.show_info()


# Forcing hidden attribute to change
cake04.glutenfree = True
print(dir(cake04))
cake04._Cake__glutenfree = True
cake04.show_info()

