import collections

Card = collections.namedtuple('Card', 'shape value')


class Whotv1(object):
    """Deck implementation v1"""
    shapes = "circle cross star square triangle whot".split() #the whole shape gang
    values = list(range(1,15)) #typical values for circle, star....
    values.extend([20]*5) #value for each of the 5 WHOTs
    
    def __init__(self):
        self._cards = [Card(shape, value) for shape in self.shapes \
            for value in self.values] #build cards
        
    def __len__(self):
        return len(self._cards) #print total value of present cards
        
    def __repr__(self):
        return str(self._cards[-10:]) #show last ten cards
    

# w = Whotv1()
# print(w)
# len(w)