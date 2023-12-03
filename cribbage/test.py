from Card import Card
from Deck import Deck
from Hand import Hand

"""
CRIBBAGE GAME
"""

deck = Deck()

deck.shuffle()

p1 = Hand()
p2 = Hand()

deck.deal_cards(6, p1)
deck.deal_cards(6, p2)

random_card = deck.random_card()  # IT IS CALLED A CUT CARD


# testHand = Hand()
# testHand.add_card(Card(1,1))
# testHand.add_card(Card(2,1))
# testHand.add_card(Card(6,1))
# testHand.add_card(Card(3,1))

print("Player 1's cards: ")
p1.display_hand()

x = random_card.read_card()
# y = Card(4,1)

print("\nCalcuating hand:")

p1.calculate_hand(random_card)

print("-------------")
p1.display_hand()

chosen_hand, crib = p1.choose_crib()

points = chosen_hand.calculate_hand()

print("\nHere is the hand that you should choose...points:", points)
chosen_hand.display_hand()

print("\nHere is what you should put in the crib: ")
crib.display_hand()
