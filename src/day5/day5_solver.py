"""
Solver for day 5: If You Give A Seed A Fertilizer
"""
import collections
from copy import deepcopy
from src.day_management.day_solver import DaySolver

RangeTuple = collections.namedtuple(
    "RangeTuple", ["dest_range_start", "source_range_start", "range_length"]
)

MAX_INT = 2147483647


class SeedMap:
    """
    Generic map, can be seed-to-soil, soil-to-fertilizer, etc.
    """

    def __init__(self, name):
        self.name = name
        self.ranges = []
        self.next_map = None

    def __str__(self):
        ranges_str = ""
        for range_tuple in self.ranges:
            ranges_str += f"({range_tuple[0]}, {range_tuple[1]}, {range_tuple[2]}), "
        return self.name + ": " + ranges_str + " -> \n" + str(self.next_map)

    def add_range(self, range_tuple):
        """
        Adds a range to the map
        """
        self.ranges.append(range_tuple)

    def add_range_for_name(self, range_tuple, name):
        """
        Adds a range to the map, if the name matches, otherwise adds it to the next map
        """
        if name == self.name:
            self.add_range(range_tuple)
        else:
            if self.next_map is None:
                self.next_map = SeedMap(name)
            self.next_map.add_range_for_name(range_tuple, name)

    def get_mapping_for_key(self, key):
        """
        Gets the mapping for a key
        """
        for range_tuple in self.ranges:
            if (
                range_tuple.source_range_start
                <= key
                < range_tuple.source_range_start + range_tuple.range_length
            ):
                return range_tuple.dest_range_start + (
                    key - range_tuple.source_range_start
                )
        return key

    def get_mapping_for_key_for_name(self, key, name):
        """
        Gets the mapping for a key, if the name matches, otherwise gets it from the next map
        """
        if name == self.name:
            return self.get_mapping_for_key(key)

        if self.next_map is not None:
            next_key = self.get_mapping_for_key(key)
            return self.next_map.get_mapping_for_key_for_name(next_key, name)
        return key


class Day5Solver(DaySolver):
    """
    Solver for day 5: If You Give A Seed A Fertilizer
    """

    def __init__(self, input_data):
        super().__init__(input_data)
        self.seeds = []
        self.seed_ranges = []
        self.seed_map = SeedMap("seed-to-soil")
        self.map_ranges = []
        self.parse_input()

    def parse_input(self):
        """
        Parses the input
        """
        i = 0
        nr_map = -1
        map_name = ""
        while i < len(self.input_data):
            line = self.input_data[i]
            i += 1
            if line.startswith("seeds"):
                seeds = line.split(":")[1].strip().split(" ")
                self.seeds = [int(seed) for seed in seeds]
            elif (len(line.strip()) > 0) and line[0].isdigit():
                dest_range_start, source_range_start, range_length = line.strip().split(
                    " "
                )
                dest_range_start = int(dest_range_start)
                source_range_start = int(source_range_start)
                range_length = int(range_length)
                range_tuple = RangeTuple(
                    dest_range_start, source_range_start, range_length
                )
                self.seed_map.add_range_for_name(range_tuple, map_name)
                self.map_ranges[nr_map].append(range_tuple)
            elif len(line.strip()) > 0:
                map_name = line.strip().split(" ")[0]
                self.map_ranges.append([])
                nr_map += 1

        for i in range(0, len(self.seeds), 2):
            self.seed_ranges.append((self.seeds[i], self.seeds[i] + self.seeds[i + 1]))

    def solve_part_one(self):
        """
        Solves part one
        """
        lowest_location = MAX_INT
        for seed in self.seeds:
            location_mapping = self.seed_map.get_mapping_for_key_for_name(
                seed, "humidity-to-location"
            )
            if location_mapping < lowest_location:
                lowest_location = location_mapping
        return lowest_location

    def solve_part_two(self):
        """
        Solves part two
        """
        seed_ranges = deepcopy(self.seed_ranges)
        for _, map_range in enumerate(self.map_ranges):
            ranges = []
            for range_tuple in map_range:
                ranges.append(range_tuple)
            new_seed_ranges = []
            while len(seed_ranges) > 0:
                start, end = seed_ranges.pop()
                for range_tuple in ranges:
                    dest = range_tuple.dest_range_start
                    src = range_tuple.source_range_start
                    length = range_tuple.range_length
                    max_start = max(start, src)
                    min_end = min(end, src + length)
                    if max_start < min_end:
                        new_seed_ranges.append(
                            (max_start - src + dest, min_end - src + dest)
                        )
                        if max_start > start:
                            new_seed_ranges.append((start, max_start))
                        if min_end < end:
                            new_seed_ranges.append((min_end, end))
                        break
                else:
                    new_seed_ranges.append((start, end))
            seed_ranges = new_seed_ranges

        return min(seed_ranges)[0]
