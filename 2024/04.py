'''

--- Advent of Code 2024 ---

Day 04: Ceres Search
https://adventofcode.com/2024/day/4

'''

class WordPuzzle:

    def __init__(self, dir: str, split: bool = False) -> None:
        with open(dir) as f:
            self.lines = f.read().splitlines()
        self.split = split

    def __repr__(self) -> str:
        count = 0
        max_idx = len(self.lines[0])
        max_idy = len(self.lines)

        if not self.split:
            for y in range(max_idy):
                for x in range(max_idx):
                    if x <= max_idx - 4:
                        count += self.get_horizontal(y, x)
                    if y <= max_idy - 4:
                        count += self.get_vertical(y, x)
                    if y <= max_idy - 4 and x <= max_idx - 4:
                        count += self.get_right_diagonal(y, x)
                        count += self.get_left_diagonal(y, x)
        else:
            for y in range(1, max_idy - 1):
                for x in range(1, max_idx - 1):
                    if self.lines[y][x] == 'A':
                        count += self.check_adjacent(y, x)

        return str(count)

    def get_horizontal(self, idy: int, idx: int) -> bool:
        return self.lines[idy][idx:idx+4][::-1] == 'XMAS' or self.lines[idy][idx:idx+4] == 'XMAS'

    def get_vertical(self, idy: int, idx: int) -> bool:
        xmas = ''.join([self.lines[y][idx] for y in range(idy, idy + 4)])
        return xmas == 'XMAS' or xmas[::-1] == 'XMAS'

    def get_right_diagonal(self, idy: int, idx: int) -> bool:
        xmas = ''.join([self.lines[idy + index][idx + index] for index in range(4)])
        return xmas == 'XMAS' or xmas[::-1] == 'XMAS'

    def get_left_diagonal(self, idy: int, idx: int) -> bool:
        xmas = ''.join([self.lines[idy + i][idx + 3 - i] for i in range(4)])
        return xmas == 'XMAS' or xmas[::-1] == 'XMAS'

    def check_adjacent(self, idy: int, idx: int) -> bool:
        left_diag = f'{self.lines[idy-1][idx-1]}A{self.lines[idy+1][idx+1]}'
        right_diag = f'{self.lines[idy-1][idx+1]}A{self.lines[idy+1][idx-1]}'

        return (left_diag == 'MAS' or left_diag[::-1] == 'MAS') and (right_diag == 'MAS' or right_diag[::-1] == 'MAS')