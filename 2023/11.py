'''

Day 11: Cosmic Expansion
https://adventofcode.com/2023/day/11

'''

class CosmicExpansion:

    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()

    # Expand the universe by duplicating and checking whether
    # a whole row does not have any galaxies ('#'). We then
    # check if a whole column does not have any galaxies.
    def expand_universe(self) -> list[str]:
        universe = list([])

        for row in self.input:
            if '#' not in row:
                universe.append(row)
            universe.append(row)

        idx = 0
        while idx != len(universe[0]):
            if '#' not in [i[idx] for i in universe]:
                for i in range(len(universe)):
                    universe[i] = universe[i][:idx] + '.' + universe[i][idx:]
                idx += 1
            idx += 1

        return universe

    # Get the galaxy positions by checking where the
    # '#' are and coordinating them to (y, x).
    def galaxy_position(self) -> list[tuple[int, int]]:
        universe = self.expand_universe()
        galaxies = list([])

        for y, row in enumerate(universe):
            for x, col in enumerate(row):
                if col == '#':
                    galaxies.append((y, x))

        return galaxies

    # Get the shortest path of each galaxies by
    # subtracting the coordinates to each other.
    # We then use abs() to make negative numbers into
    # positive numbers.
    def find_path_total(self) -> None:
        total = 0
        galaxies = self.galaxy_position()

        for y, origin in enumerate(galaxies):
            for galaxy in galaxies[y+1:]:
                total += abs(origin[0] - galaxy[0]) + abs(origin[1] - galaxy[1])

        return total