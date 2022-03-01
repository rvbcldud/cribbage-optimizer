class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def display_hand(self):
        for i in self.cards:
            print('\t' + i.read_card())

