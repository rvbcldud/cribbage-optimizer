class Card:
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

    def __init__(self, key, suit):
        self.key = key
        self.suit = suit
        if key < 10:
            self.value = key
        else:
            self.value = 10

    def read_card(self):
        key = Card.KEYS.get(self.key)  # 1 -> Ace
        suit = Card.SUITS.get(self.suit)  # 1 -> Diamonds
        card_name = key + " of " + suit

        return card_name
    
    def parse_card(card):
        if (len(card) < 2 or len(card) > 3):
            raise ValueError("Card given not in the correct format")

        key = card[0:len(card) - 1]
        suit = card[len(card) - 1]

        # print("Card: ", card)
        # print("key:", key, "suit:", suit)

        # Checking if card rank is a digit between 2-10
        if key.isdigit():
            if int(key) >= 2 and int(key) <= 10:
                key = int(key) # Keep it!
            else:
                raise ValueError("Invalid card rank; must be A,1,2,...,K")
        # Otherwise matching it to correct face card or ace
        else:
            if key == "J":
                key = 11
            elif key == "Q":
                key == 12
            elif key == "K":
                key = 13
            elif key == "A":
                key = 1
            else:
                raise ValueError("Invalid card rank; must be A,1,2,...,K")
        
        if suit == "H":
            suit = 0
        elif suit == "D":
            suit = 1
        elif suit == "C":
            suit = 2
        elif suit == "S":
            suit = 3
        else:
            raise ValueError("Invalid suit; must be H, D, C, or S")

        # print("Card has key:", key, "and suit:", suit)
        
        return Card(key, suit)
