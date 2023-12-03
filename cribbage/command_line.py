import sys

from cribbage import Hand, Deck

def main():
    print("Welcome to cribbage-optimizer!")
    while True:
        mode = start()
        # User defined hand:
        if mode == 1:
            hand = input("Please input 6 cards: ")
            parsed_hand = Hand.read_hand(hand)
            
            print("\nThe hand you imported: ")
            parsed_hand.display_hand()

            print("\nThe following is the optimal chosen hand and crib for"
                " the greatest number of guaranteed points\n")
            best_hand, best_crib, points = Hand.choose_crib(parsed_hand)
            print("Best hand:")
            best_hand.display_hand()

            print("Crib:")
            best_crib.display_hand()

            print("With a guaranteed number of points of:", points)
            
            loop_ask()




        # Randomized hand:
        if mode == 0:
            print("Here is a randomly dealt hand in cribbage:")

            deck = Deck()
            deck.shuffle()
            hand = Hand()
            deck.deal_cards(6, hand)

            hand.display_hand()


            print("\nThe following is the optimal chosen hand and crib for"
                " the greatest number of guaranteed points\n")

            best_hand, best_crib, points = Hand.choose_crib(hand)
            print("Best hand:")
            best_hand.display_hand()

            print("Crib:")
            best_crib.display_hand()

            print("With a guaranteed number of points of:", points)

            loop_ask()
            

    


def start():
    while True:
        mode = input("Would you like to input a hand (h) or "
                "draw randomly (r)? ").lower()
        if mode == "r":
            return 0
        elif mode == "h":
            return 1
        else:
            print("Invalid input. Try again")


def loop_ask():
    while True:
        loop = input("Would you like to use the optimizer again? (y/n) ").lower()

        if loop == "y":
            break
        elif loop == "n":
            print("Thank you for using Cribbage Hand Optimizer!")
            sys.exit()
        else:
            print("Invalid input. Try again")
