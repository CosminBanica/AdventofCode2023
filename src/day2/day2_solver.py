"""
Solver for day 2: Cube Conundrum
"""
import collections
from src.day_management.day_solver import DaySolver

MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12

Game = collections.namedtuple("Game", ["nr", "reveals"])


class Day2Solver(DaySolver):
    """
    Solver for day 2: Cube Conundrum
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.games = []
        self.parse_input()

    def parse_input(self):
        """
        Parses the input data into a list of games
        """
        for line in self.input_data:
            line = line.strip()
            line_parts = line.split(":")
            game_nr = int(line_parts[0].split(" ")[1])
            cube_reveals = line_parts[1].split(";")
            cubes = []
            for cube_reveal in cube_reveals:
                cube_reveal = cube_reveal.strip()
                cube_reveal_parts = cube_reveal.split(",")

                reveal = {}
                for cube_reveal_part in cube_reveal_parts:
                    cube_reveal_part = cube_reveal_part.strip()
                    color_reveal = cube_reveal_part.split(" ")
                    cube_nr = int(color_reveal[0])
                    cube_color = color_reveal[1]
                    reveal[cube_color] = cube_nr

                cubes.append(reveal)

            self.games.append(Game(game_nr, cubes))

    def solve_part_one(self):
        """
        Solves part one
        """
        possible_games_nr_sum = 0
        for game in self.games:
            for reveal in game.reveals:
                if "blue" in reveal and reveal["blue"] > MAX_BLUE:
                    break
                if "green" in reveal and reveal["green"] > MAX_GREEN:
                    break
                if "red" in reveal and reveal["red"] > MAX_RED:
                    break
            else:
                possible_games_nr_sum += game.nr

        return possible_games_nr_sum

    def solve_part_two(self):
        """
        Solves part two
        """
        power_sum = 0
        for game in self.games:
            minimum_blue = 0
            minimum_green = 0
            minimum_red = 0
            for reveal in game.reveals:
                if "blue" in reveal and reveal["blue"] > minimum_blue:
                    minimum_blue = reveal["blue"]
                if "green" in reveal and reveal["green"] > minimum_green:
                    minimum_green = reveal["green"]
                if "red" in reveal and reveal["red"] > minimum_red:
                    minimum_red = reveal["red"]
            power = minimum_blue * minimum_green * minimum_red
            power_sum += power

        return power_sum
