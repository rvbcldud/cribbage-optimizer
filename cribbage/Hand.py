from itertools import combinations
from random import choice
from .Card import Card

import numpy as np


class Hand:
    def __init__(self, card_list=None):
        """
        Initializes a hand of cards
        """
        if card_list != None:
            self.cards = card_list
        else:
            self.cards = []

    def add_card(self, card):
        """
        Adds given card to current hand
        """
        self.cards.append(card)
        return self

    def remove_card(self, card):
        """
        Removes given card from current hand
        """
        self.cards.remove(card)
        return self

    def display_hand(self):
        """
        Displays all cards in hand, takes no parameters
        """
        for i in self.cards:
            print("\t" + i.read_card())
    
    def has_duplicate(self):
        for i in self.cards:
            for j in self.cards:
                if i.key == j.key:
                    return True
        return False

    def calculate_hand(self, cut_card=None):
        """
        Calculates the score of a given set of cards. It does this by calculating
        each type of score:
        - Pairs
        - Runs
        - Fifteens
        """


        """
        Calculate all 5, 4, 3, 2 combinations
        This means we need to split up all kinds of earning points
        - Pairs: Check if there is more than one of each card in hand
        - Runs: Look at every 3, 4, and 5 card combination
          - If one 5, no 4s
          - If one or two 4, no 3s
            - Two 4 when they don't equal each other
        - 15s: If 5 long 15, no 4s, etc.
          - Can only be 1 or 2 4s, but can also have 4s or 2s
          - To check for duplicates, compare sorted lists
        """

        if cut_card is not None:
            hand = self.add_card(cut_card)
        else:
            hand = self

        def populate_combos(hand):
            combos = []
            for i in range(len(hand.cards)):
                # Make all different length combinations from 1 -> n
                temp = [list(x) for x in combinations(hand.cards, i + 1)]
                if len(temp) > 0:
                    combos.extend(temp)
            return combos

        combos = populate_combos(hand)

        def calculate_pairs(hand):
            # Create a list of cards, but only the keys
            key_list = []
            for card in hand.cards:
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

            return points

        def calculate_runs(combo_list):
            def check_consecutive(lst):
                # Checks to see if the list of integers is consecutive
                n = len(lst) - 1
                return sum(np.diff(lst) == 1) >= n

            run_list = []

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
                    run_list.append(hand)

            # Filter the list of runs for the only possible combinations
            # Rules:
            # - Runs: Look at every 3, 4, and 5 card combination
            #   - If one 5, no 4s
            #   - If one or two 4, no 3s
            #   - If 2 threes, there must be a pair

            run_list = [x for x in run_list if len(x) == max_len]

            points = 0

            three_count = 0
            four_count = 0
            five_count = 0

            # TODO: Add counters to enforce the filter rules
            for i in run_list:
                # Turn card list into hand object
                i_hand = Hand(i)
                if len(i) == 5:
                    five_count += 1
                    points += 5
                elif len(i) == 4:
                    if five_count > 0:
                        continue
                    four_count += 1
                    points += 4
                elif len(i) == 3:
                    # If there are 2 three runs and no pairs ... don't count
                    if three_count >= 1 and i_hand.has_duplicate():
                        continue
                    # If there are any four runs, no three runs
                    elif four_count > 0:
                        continue
                    else:
                        three_count += 1
                        points += 3

            return points

        def calculate_fifteen(combo_list):
            fifteen_list = []
            for hand in combo_list:
                temp = []
                for card in hand:
                    temp.append(card.value)
                # Checks if the pair/set is equal to 15. If so, add to list of 15s
                if sum(temp) == 15:
                    fifteen_list.append(temp)

            points = 0

            for i in fifteen_list:
                points += 2

            return points

        pairs = calculate_pairs(self)
        runs = calculate_runs(combos)
        fifteens = calculate_fifteen(combos)

        total_points = pairs + runs + fifteens

        # Remove cut card and return the hand to its original state
        if cut_card:
            self.remove_card(cut_card)

        return total_points

    def choose_crib(self):
        """
        From the present hand of 6 cards, choose_crib() will calculate
        all the possibile hands within it and output the best possible
        hand and crib selection with the greatest number of guaranteed points
        """
        combo_list = []

        # Create a list of all 4 card hands from a 6 card hand
        for combo in combinations(self.cards, 4):
            temp = Hand()
            for card in combo:
                temp.add_card(card)
            combo_list.append(temp)

        best_hands = []
        max_points = 0

        # Calculates value of the 4 card sub-hands of the current 6 card hand
        for hand in combo_list:
            points = hand.calculate_hand()
            if points > max_points:
                max_points = points

            best_hands.append((points, hand))

        # Filters the list of points and hands to only give a list of the
        # hands with the highest value
        best_hands = [x[1] for x in best_hands if x[0] == max_points]

        chosen_hand = choice(best_hands)
        # Calculate the gaurenteed number of points of chosen hand

        # Finds the 2 cards that are not included in the best hand, and puts
        # them into the crib
        crib_diff = list(set(self.cards) - set(chosen_hand.cards))
        crib_hand = Hand()
        for i in crib_diff:
            crib_hand.add_card(i)

        return chosen_hand, crib_hand, max_points
    
    def read_hand(hand):
        """
        Takes a series of 7 cards, the first of which is the cut card
        and converts it into a language python can understand
        """
        parsed_hand = Hand()
        cards = hand.split()
        for card in cards:
            parsed_hand.add_card(Card.parse_card(card))

        return parsed_hand

        
