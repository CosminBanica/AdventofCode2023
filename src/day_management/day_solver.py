"""
This module contains the base class for all day solvers.
"""
from abc import ABC, abstractmethod


class DaySolver(ABC):
    """
    Base class for all day solvers.
    """

    def __init__(self, input_data):
        self.input_data = input_data

    @abstractmethod
    def solve_part_one(self):
        """
        Solves part one of the day's puzzle.
        """

    @abstractmethod
    def solve_part_two(self):
        """
        Solves part two of the day's puzzle.
        """
