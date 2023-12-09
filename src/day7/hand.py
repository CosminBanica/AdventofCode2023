"""
Hand behaviour
"""
from enum import Enum
from src.day7.card import NORMAL_CARD_VALUES, JOKER_CARD_VALUES


class Type(Enum):
    """
    Enum for the type of hand
    """

    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7
    UNSET = 8


class BaseHand:
    """
    Base class for a hand
    """

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.pairs = set()
        self.triples = set()
        self.quads = set()
        self.quints = set()
        self.type = Type.HIGH_CARD

    def set_type(self):
        """
        Sets the type of hand
        """
        if len(self.quints) == 1:
            self.type = Type.FIVE_OF_A_KIND
        elif len(self.quads) == 1:
            self.type = Type.FOUR_OF_A_KIND
        elif len(self.triples) == 1 and len(self.pairs) == 1:
            self.type = Type.FULL_HOUSE
        elif len(self.triples) == 1:
            self.type = Type.THREE_OF_A_KIND
        elif len(self.pairs) == 2:
            self.type = Type.TWO_PAIR
        elif len(self.pairs) == 1:
            self.type = Type.PAIR
        else:
            self.type = Type.HIGH_CARD

    def add_card_to_pairs(self, card):
        """
        Adds a card to the correct pair type
        """
        if self.cards.count(card) == 2:
            self.pairs.add(card)
        if self.cards.count(card) == 3:
            self.triples.add(card)
        if self.cards.count(card) == 4:
            self.quads.add(card)
        if self.cards.count(card) == 5:
            self.quints.add(card)

    def __str__(self):
        return str(self.cards) + " " + str(self.type) + " Base Hand"


class NormalHand(BaseHand):
    """
    Class for a normal hand
    """

    def __init__(self, cards, bid):
        super().__init__(cards, bid)
        for card in self.cards:
            self.add_card_to_pairs(card)
        self.set_type()

    def __str__(self):
        return str(self.cards) + " " + str(self.type) + " Normal Hand"


class JokerHand(BaseHand):
    """
    Class for a joker hand
    Every J just acts like whatever card would make the best hand
    If all cards are J, then the hand is a five of a kind type
    """

    def __init__(self, cards, bid):
        super().__init__(cards, bid)
        for card in self.cards:
            if card != "J":
                self.add_card_to_pairs(card)
            elif self.cards.count(card) == 5:
                self.quints.add(card)
        self.joker_count = self.cards.count("J")

        if len(self.quints) == 0 and self.joker_count > 0:
            self.convert_jokers_in_pairs()

        self.set_type()

    def convert_jokers_in_pairs(self):
        """
        Converts Jokers into pairs
        """
        if len(self.quads) == 1:
            quad = self.quads.pop()
            self.quints.add(quad)
        elif len(self.triples) == 1:
            triple = self.triples.pop()
            if self.joker_count == 1:
                self.quads.add(triple)
            else:
                self.quints.add(triple)
        elif len(self.pairs) > 0:
            pair = self.pairs.pop()
            if self.joker_count == 1:
                self.triples.add(pair)
            elif self.joker_count == 2:
                self.quads.add(pair)
            else:
                self.quints.add(pair)
        else:
            if self.joker_count == 1:
                self.pairs.add("A")
            elif self.joker_count == 2:
                self.triples.add("A")
            elif self.joker_count == 3:
                self.quads.add("A")
            else:
                self.quints.add("A")

    def __str__(self):
        return str(self.cards) + " " + str(self.type) + " Joker Hand"


def compare_hands(hand1, hand2):
    """
    Compares two hands
    Higher hand type wins
    If same hand type, iterate through cards, until one is higher
    """
    card_value_map = None
    if isinstance(hand1, JokerHand):
        card_value_map = JOKER_CARD_VALUES
    else:
        card_value_map = NORMAL_CARD_VALUES

    if hand1.type.value > hand2.type.value:
        return 1
    if hand1.type.value < hand2.type.value:
        return -1
    if hand1.type.value == hand2.type.value:
        for card1, card2 in zip(hand1.cards, hand2.cards):
            if card_value_map[card1] > card_value_map[card2]:
                return 1
            if card_value_map[card1] < card_value_map[card2]:
                return -1
    return 0
