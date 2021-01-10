import random
import collections
from card_filter import filter_card



Card = collections.namedtuple('Card', 'shape value')


class Whotv2(object):
    shapes = "circle cross star square triangle whot".split()
    values = list(range(1,15))
    values.extend([20]*5) #value for each of the 5 WHOTs
    
    def __init__(self, shuffle=False):
        self._cards = list(filter(filter_card, [Card(shape, value) for shape in self.shapes \
            for value in self.values])) #build cards
        if shuffle:
            random.shuffle(self._cards) #shuffle deck
        
    def __len__(self):
        return len(self._cards) #print total value of present cards
        
    def __repr__(self):
        return str(self._cards[-10:]) #show last ten cards
    
    def __setitem__(self, pos, card):
        self._cards[pos] = card #card should be Card namedtuple

    

# w2 = Whotv2()
# print(w2)
# print("\nDeck consists a total of {} playing cards".format(len(w2))) #54