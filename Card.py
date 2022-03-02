class Card:
    KEYS = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
         6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack',
         12: 'Queen', 13: 'King'}

    SUITS = {0: 'Hearts', 1: 'Diamonds', 2: 'Clubs', 3: 'Spades'}

    def __init__(self, key, suit):
        self.key = key
        self.suit = suit
        if key < 10:
            self.value = key
        else:
            self.value = 10

    def read_card(self):
        key = self.KEYS.get(self.key) # 0 -> Ace
        suit = self.SUITS.get(self.suit) # 1 -> Diamonds
        card_name = key + ' of ' + suit

        return card_name
