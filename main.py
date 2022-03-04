from Deck import Deck
from Hand import Hand
from Card import Card

'''
CRIBBAGE GAME
'''

deck = Deck()

deck.shuffle()

p1 = Hand()
p2 = Hand()

deck.deal_cards(6, p1)
deck.deal_cards(6, p2)

random_card = deck.random_card() # IT IS CALLED A CUT CARD  

p1.remove_card(p1.cards[0])
p1.remove_card(p1.cards[1])

print('Player 1\'s cards: ')
p1.display_hand()

x = random_card.read_card()

print('\t' + x)

print('\nCalcuating hand:')
print('\t' + x)
p1.calculate_hand(random_card)


