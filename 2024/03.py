'''

--- Advent of Code 2024 ---

Day 03: Mull It Over
https://adventofcode.com/2024/day/3

'''

class Computer:

    def __init__(self, dir: str) -> None:
        with open(dir) as f:
            self.memory = f.read().splitlines()
        self.mul_enabled = True

    def __repr__(self) -> str:
        result = 0

        for line in self.memory:
            result += self.find_mul(line, True)

        return str(result)

    def find_mul(self, corrupted: str, do_functions: bool = False) -> int:
        result = 0

        for idx in range(len(corrupted) - 3):
            if do_functions and corrupted[idx:idx+4] == 'do()':
                self.mul_enabled = True
            if do_functions and corrupted[idx:idx+7] == "don't()":
                self.mul_enabled = False

            if corrupted[idx:idx+4] == 'mul(':
                digits = self.parse_values(corrupted, idx + 2)
                if digits and not do_functions:
                    result += digits[0] * digits[1]
                elif digits and do_functions and self.mul_enabled:
                    result += digits[0] * digits[1]

        return result

    def parse_values(self, corrupted:str, idx: int) -> tuple[int, int]:
        parsed = ''

        while corrupted[idx] != ')':
            idx += 1
            parsed += corrupted[idx]

        return self.tokenizer(parsed)

    def tokenizer(self, value: str) -> tuple[int, int]:
        digits = value[1:-1].split(',')

        if digits[0].isdigit() and digits[1].isdigit():
            return (int(digits[0]), int(digits[1]))
        return None