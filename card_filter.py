excluded_cards = [
    [6,9,10,11,12,13,14,20], #star
    [4,6,8,9,12,20], #cross & square
    [6,9,20], #cirlce & triangle
    #list(range(1,15)), #whot
]



def filter_card(card):
    """return True only when a shape does not contain values \
        from its exclusive list of values"""
    if (card.shape == 'star') and (card.value not in excluded_cards[0]):
        return True
    if (card.shape == 'cross' or card.shape == "square") and (card.value not in excluded_cards[1]):
        return True
    if (card.shape == 'circle' or card.shape == 'triangle') and (card.value not in excluded_cards[2]):
        return True
    if (card.shape == 'whot') and (card.value == 20):
        return True
    return False


# #asserts to False; no 20 of star
# assert(filter_card(Card(shape='star', value=20)) == False)

# #asserts to True
# assert(filter_card(Card(shape='whot', value=20)) == True)