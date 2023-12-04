"""
Solver for day 4: Scratchcards
"""
import collections
from src.day_management.day_solver import DaySolver

Card = collections.namedtuple(
    "Card", ["nr", "winning_numbers", "chosen_numbers", "copies"]
)


def get_card_points(card):
    """
    Gets the points for a card
    """
    points = 0
    for chosen_number in card.chosen_numbers:
        if chosen_number in card.winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points


def get_matches(card):
    """
    Gets the matches for a card
    """
    matches = 0
    for chosen_number in card.chosen_numbers:
        if chosen_number in card.winning_numbers:
            matches += 1
    return matches


class Day4Solver(DaySolver):
    """
    Solver for day 4: Scratchcards
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.cards = []
        self.parse_input()

    def parse_input(self):
        """
        Parses the input data
        """
        for line in self.input_data:
            line = line.strip()
            card_and_numbers = line.split(":")
            card_nr = card_and_numbers[0].split(" ")
            card_nr = int(card_nr[len(card_nr) - 1])
            winning_and_chosen_numbers = card_and_numbers[1].split("|")

            winning_numbers = winning_and_chosen_numbers[0].strip().split(" ")
            chosen_numbers = winning_and_chosen_numbers[1].strip().split(" ")

            winning_numbers = [int(x) for x in winning_numbers if x != ""]
            chosen_numbers = [int(x) for x in chosen_numbers if x != ""]

            self.cards.append(Card(card_nr, winning_numbers, chosen_numbers, 1))

    def solve_part_one(self):
        """
        Solves part one
        """
        points_sum = 0
        for card in self.cards:
            points_sum += get_card_points(card)
        return points_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        total_cards = 0
        for i, card in enumerate(self.cards):
            matches = get_matches(card)
            for j in range(1, matches + 1):
                if i + j < len(self.cards):
                    self.cards[i + j] = Card(
                        self.cards[i + j].nr,
                        self.cards[i + j].winning_numbers,
                        self.cards[i + j].chosen_numbers,
                        self.cards[i].copies + self.cards[i + j].copies,
                    )
                else:
                    break
            total_cards += self.cards[i].copies

        return total_cards
