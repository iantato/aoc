'''

--- Advent of Code 2024 ---
Day 07: Bridge Repair

https://adventofcode.com/2024/day/7

'''

class Calibration:

    def __init__(self, dir: str) -> None:
        with open(dir) as f:
            self.calibration = f.read().splitlines()


    def __repr__(self) -> str:
        total_calibration = 0

        for i in self.calibration:
            expected, numbers = self.parse(i)
            if self.calculate(expected, numbers):
                total_calibration += expected

        return str(total_calibration)

    def parse(self, line: str) -> tuple[int, list[int]]:
        expected, numbers = line.split(':')
        numbers = list(map(int, numbers.lstrip().split(' ')))

        return (int(expected), numbers)

    def calculate(self, expected: int, numbers: list[int]) -> bool:
        if numbers[0] > expected:
            return False
        if len(numbers) == 1:
            return numbers[0] == expected

        n1, n2 = numbers[0], numbers[1]
        rest = numbers[2:]

        if self.calculate(expected, [n1 + n2] + rest):
            return True

        if self.calculate(expected, [n1 * n2] + rest):
            return True

        if self.calculate(expected, [int(str(n1) + str(n2))] + rest):
            return True

        return False