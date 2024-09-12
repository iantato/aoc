'''

Day 11: Cosmic Expansion
https://adventofcode.com/2023/day/11

'''

class CosmicExpansion:

    # Multiplier used for how much you want to expand the universe.
    # Keep in mind to always -1 it if multiplier != 1 because of the
    # extra character we have in each expansion.
    MULTIPLIER = 1000000 - 1

    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()

    # Get all the galaxy positions and store them in (y, x) format.
    def galaxy_positions(self) -> list[tuple[int, int]]:
        galaxies = list([])

        for y, row in enumerate(self.input):
            for x, col in enumerate(row):
                if col == '#':
                    galaxies.append((y, x))

        return galaxies

    # Find the shortest path between all galaxies pair.
    def find_path_total(self) -> None:
        total = 0
        galaxies = self.galaxy_positions()

        # Get coordinates of the rows and columns that needs to be expanded so
        # that we can use it in the calculation later. This is so that we don't
        # have to brute-force the expansion and instead can just use calculations
        # by finding the position of the expansion and the galaxies.
        expanded_rows = [x for x, i in enumerate(self.input) if '#' not in i]
        expanded_col = [x for x, i in enumerate(self.input) if '#' not in [i[x] for i in self.input]]

        for y, origin in enumerate(galaxies):
            for galaxy in galaxies[y+1:]:
                total += abs(origin[0] - galaxy[0]) + (len([i for i in expanded_rows if i >= min(origin[0], galaxy[0]) and i <= max(origin[0], galaxy[0])]) * self.MULTIPLIER)
                total += abs(origin[1] - galaxy[1]) + (len([i for i in expanded_col if i >= min(origin[1], galaxy[1]) and i <= max(origin[1], galaxy[1])]) * self.MULTIPLIER)

        return total