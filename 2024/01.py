'''

--- Advent of Code 2024 ---

Day 01: Historian Hysteria
https://adventofcode.com/2024/day/1

'''

class Distance:

    def __init__(self, data: str) -> None:
        with open(data) as f:
            self.data = f.read().splitlines()

    # Part 01
    def get_distance(self) -> int:
        """
        Part 01 Solution.
        """
        gap = 0
        first_list = []
        second_list = []

        for i in self.data:
            first_list.append(i.split('  ')[0])
            second_list.append(i.split('  ')[1])

        first_list = sorted(first_list)
        second_list = sorted(second_list)

        for i in range(len(first_list)):
            gap += abs(int(first_list[i]) - int(second_list[i]))

        return gap

    # Part 02
    def similarity_score(self) -> int:
        """
        Part 02 Solution.
        """
        similarity = 0
        first_list = []
        second_list_counter = {}

        for i in self.data:
            first_list.append(int(i.split('  ')[0]))
            second_list_counter[int(i.split('  ')[1])] = second_list_counter.get(int(i.split('  ')[1]), 0) + 1

        for i in first_list:
            similarity += second_list_counter.get(i, 0) * i

        return similarity