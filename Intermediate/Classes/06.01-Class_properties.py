class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, text, filling, glutenfree=False):
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
        if self.kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''

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
        if len(self.__text) > 0:
            print('Text:    {}'.format(self.__text))
        print('--'*10)

    def set_fillling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            self.__text = ''

    Text = property(__get_text, __set_text, None, 'Text of the cake.')

baker_offer = []
cake01 = Cake('Vanilla cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'tExT', 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolate', ['chocolade'], 'tEXt2', '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], 'TexT3', '', True)
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'teXT4', 'cocoa')


print('Today in the offer:')
for c in Cake.bakery_offer:
    c.show_info()

cake02.Text = 'ff'
cake02.show_info()

print(cake01.Text)

