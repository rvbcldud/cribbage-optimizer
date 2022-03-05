from itertools import combinations
import numpy as np

class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        return self

    def remove_card(self, card):
        self.cards.remove(card)
        return self

    def display_hand(self):
        for i in self.cards:
            print('\t' + i.read_card())

    def calculate_hand(self, cut_card=None):
        '''
        Calculate all 5, 4, 3, 2 combinations
        This means we need to split up all kinds of earning points
        - Pairs: Check if there is more than one of each card in hand
        - Runs: Look at every 3, 4 card combination
          - If one 5, no 4s
          - If one or two 4, no 3s
            - Two 4 when they don't equal each other
        - 15s: If 5 long 15, no 4s, etc.  
          - Can only be 1 or 2 4s, but can also have 4s or 2s
          - To check for duplicates, compare sorted lists
          - If calue of card >= 10, real value is 10
          - Create new variable value and change what is currently value to key
            - Set this when you populate the deck
        '''

        if cut_card is not None:
            hand = self.add_card(cut_card)
            print('CUT CARD DETECTED')

        # TODO incorporate cut card!

        def populate_combos(self):
            self.display_hand()
            combos = []
            for i in range(len(self.cards)):
                temp = [list(x) for x in combinations(self.cards, i)]
                if len(temp) > 0:
                    combos.extend(temp)
            return combos

        combos = populate_combos(hand)

        def calculate_pairs(self):
            print('CALCULATING PAIRS')
            # Create a list of cards, but only the keys
            key_list = []
            for card in self.cards:
                key_list.append(card.key)
            key_list = sorted(key_list)

            # Search for duplicates of a number and populate a list with how
            # many duplicates there are in a number
            final_list = []
            for i in key_list:
                temp = []
                for j in key_list:
                    if i == j:
                        temp.append(j)
                if len(temp) > 1 and temp not in final_list:
                    final_list.append(temp)

            points = 0

            # Calculate points based on the found pairs
            for i in final_list:
                if len(i) == 2:
                    points += 2
                elif len(i) == 3:
                    points += 6
                elif len(i) == 4:
                    points += 8


            print(final_list)

            return points

        def calculate_runs(combo_list):
            print('CALCULATING RUNS')
            run_list = []
            def check_consecutive(lst):
                # Checks to see if the list of integers is consecutive
                n = len(lst) - 1
                return(sum(np.diff(lst) == 1) >= n)

            for hand in combo_list:
                key_list = []
                max_len = 3
                for card in hand:
                    key_list.append(card.key)
                if check_consecutive(key_list) and len(key_list) > 2:
                    if len(key_list) == 4:
                        max_len = 4
                    elif len(key_list) == 5:
                        max_len = 5
                    print(key_list)
                    run_list.append(hand)
                    print('cards :')
                    for card in hand:
                        print(card.read_card())

            run_list=[x for x in run_list if len(x)==max_len]

            points = 0

            for i in run_list:
                if len(i) == 3:
                    points += 3
                elif len(i) == 4:
                    points += 4
                elif len(i) == 5:
                    points += 5

            return points


        def calculate_fifteen(combo_list):
            print('CALCULATING 15s')
            fifteen_list = []
            for hand in combo_list:
                temp = []
                for card in hand:
                    temp.append(card.value)
                # Checks if the pair is equal to 15. If so, add to list of 15s
                if sum(temp) == 15:
                    fifteen_list.append(temp)
                    
            print(fifteen_list)

            points = 0

            for i in fifteen_list:
                points += 2

            return points



        pairs = calculate_pairs(self)
        runs = calculate_runs(combos)
        fifteens = calculate_fifteen(combos)

        total_points = pairs + runs + fifteens

        print('TOTAL POINTS:', total_points)

        self.remove_card(cut_card)

        return total_points





