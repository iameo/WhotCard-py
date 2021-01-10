class Player:
    """an awful, awful player class"""
    def __init__(self, name='NotSoGoodImplementation'):
        self.name = name
        self.__hand = []

    @property
    def _hand(self): #not entirely necessary but let's play safe
        return self.__hand
        
    def deal(self, deck, size=4): #WHOT game usually defaults to 4 draws
        for num in range(size):
            self._hand.append(deck.drawCard())
        
    def showHand(self):
        return '{player} has {_hand} in hand'.format(player=self.name, _hand=self._hand)
    
    def playHand(self, position=-1): #pop last card by default
        card_in_hand = len(self._hand)
        if position > card_in_hand:
            raise IndexError("Max index wrt cards in hand is {}".format(card_in_hand - 1))
        return self._hand.pop(position)
    
    def sizeHand(self):
        return sum(card.value for card in self._hand)
    
    def compareHand(self, other):
        """
        for when there's a winner in grouping more than 2 \
        and a card count is used for subsequent winners
        """
        if self.sizeHand() < other.sizeHand():
            return '{player} wins!'.format(player=self.name)
        elif self.sizeHand() == other.sizeHand():
            return 'draw!'
        else:
            return '{player} wins!'.format(player=other.name)
        
    def inspect(self):
        return bool(len(self._hand)) #if empty return False; no cards
            
    def __repr__(self):
        return reprlib.repr(self._hand) #[Card('star',3)....]