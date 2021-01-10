class Card(object):
    """a card object implementation"""
    def __init__(self, shape, value):
        self._shape = shape #shape: circle, triangle....
        self._value = value #3,5,2....
        
    def __str__(self):
        cls = type(self)
        return '{cls}({shape}, {value})'.format(cls=str(cls.__name__), shape=self._shape, value=self._value)
    
    
    
# card = Card('star', 3) #3 of star
# print(card)
# card._shape = 'cirlce'
# card._value = 8
# print(card)