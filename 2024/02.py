'''

--- Advent of Code 2024 ---

Day 02: Historian Red-Nosed Reports
https://adventofcode.com/2024/day/2


'''

from math import copysign

class SafeReports:

    def __init__(self, dir: str) -> None:
        with open(dir) as f:
            self.reports = f.read().splitlines()

    def __repr__(self) -> str:
        safe = 0

        for i in self.reports:
            report = list((map(int, i.split(' '))))

            if self.get_safe(report):
                """
                Part 01 Solution.
                """
                safe += 1
            else:
                """
                Part 02 Solution.
                """
                for level in range(len(report)):
                    if self.get_safe(report[:level] + report[level + 1:]):
                        safe += 1
                        break

        return f'{safe} total safe reports.'

    def check_min(self, data: list) -> bool:
        return abs(min(map(abs, data))) >= 1

    def check_max(self, data: list) -> bool:
        return abs(max(map(abs, data))) <= 3

    def check_sign(self, data: list) -> bool:
        return copysign(1, max(data)) == copysign(1, min(data))

    def get_safe(self, report: list) -> bool:
        """
        Checks whether the report is safe or unsafe based on the
        given conditions.

        Returns:
            A boolean to check if the report is safe or not.
        """
        # Get the difference between all the elements in the report.
        normalized = [report[i + 1] - report[i] for i in range(len(report) - 1)]

        if self.check_min(normalized) and self.check_max(normalized) and self.check_sign(normalized):
            return True
        return False