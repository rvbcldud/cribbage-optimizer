from itertools import combinations
import numpy as np

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

    def calculate_hand(self, cut_card):
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
        hand = self

        def populate_combos(self):
            self.display_hand()
            combos = []
            for i in range(len(self.cards) + 1):
                temp = [list(x) for x in combinations(self.cards, i)]
                if len(temp) > 0:
                    combos.extend(temp)
            return combos

        combos = populate_combos(hand)

        def calculate_pairs(self):
            # Create a list of cards, but only the keys
            key_list = []
            for card in self.cards:
                key_list.append(card.key)
            key_list = sorted(key_list)


            # Search for duplicates of a number and populate a list with how
            # many duplicates there are in a number: in the form of a list
            final_list = []
            for i in key_list:
                temp = []
                for j in key_list:
                    if i == j:
                        temp.append(j)
                if len(temp) > 1 and temp not in final_list:
                    final_list.append(temp)

        def calculate_runs(combo_list):
            print('CALCULATING RUNS')
            run_list = []
            def check_consecutive(lst):
                n = len(lst) - 1
                return(sum(np.diff(sorted(lst)) == 1) >= n)


            # TODO Still need to weed out sublists of 4s

            for hand in combo_list:
                key_list = []
                for card in hand:
                    key_list.append(card.key)
                if check_consecutive(key_list) and len(key_list) > 2:
                    print(key_list)
                    run_list.append(hand)
                    print('cards :')
                    for card in hand:
                        print(card.read_card())



        calculate_pairs(self)
        calculate_runs(combos)






