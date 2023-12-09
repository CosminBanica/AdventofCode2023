"""
Solver for day 7: Camel Cards
"""
from functools import cmp_to_key
from src.day_management.day_solver import DaySolver
from src.day7.hand import NormalHand, JokerHand, compare_hands


class Day7Solver(DaySolver):
    """
    Solver for day 7: Camel Cards
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.normal_hands = []
        self.joker_hands = []
        for line in input_data:
            hand, bid = line.split(" ")
            hand = list(hand.strip())
            bid = bid.strip()
            self.normal_hands.append(NormalHand(hand, bid))
            self.joker_hands.append(JokerHand(hand, bid))

    def solve_part_one(self):
        """
        Solves part one
        """
        self.normal_hands.sort(key=cmp_to_key(compare_hands))
        total_winnings = 0
        for i, hand in enumerate(self.normal_hands):
            total_winnings += hand.bid * (i + 1)

        return total_winnings

    def solve_part_two(self):
        """
        Solves part two
        """
        self.joker_hands.sort(key=cmp_to_key(compare_hands))
        total_winnings = 0
        for i, hand in enumerate(self.joker_hands):
            total_winnings += hand.bid * (i + 1)

        return total_winnings
