from cribbage import Card
from random import shuffle, choice


class Deck:
    KEYS = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King",
    }

    SUITS = {0: "Hearts", 1: "Diamonds", 2: "Clubs", 3: "Spades"}

    def __init__(self):
        self.cards = []
        self.populate_deck()

    def populate_deck(self):
        for suit in self.SUITS:
            for key in self.KEYS:
                card = Card(key, suit)
                self.cards.append(card)

    def shuffle(self):
        shuffle(self.cards)

    def deal_cards(self, card_num, hand):
        for i in range(card_num):
            hand.add_card(self.cards[i])
            self.cards.remove(self.cards[i])

    def random_card(self):
        card = choice(self.cards)
        self.cards.remove(card)
        return card
