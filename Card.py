class Card:
    VALUES = {0: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
         6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack',
         12: 'Queen', 13: 'King'}

    SUITS = {0: 'Hearts', 1: 'Diamonds', 2: 'Clubs', 3: 'Spades'}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def read_card(self):
        value = self.VALUES.get(self.value) # 0 -> Ace
        suit = self.SUITS.get(self.suit) # 1 -> Diamonds
        card_name = value + ' of ' + suit

        return card_name
