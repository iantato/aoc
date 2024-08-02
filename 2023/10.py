'''

--- Advent of Code 2023 ---

Day 10: Pipe Maze
https://adventofcode.com/2023/day/10

'''

import os
from collections import deque

class PipeMaze():

    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()
        
        self.visited = set()
        self.neighbors = deque([])

    def find_start(self) -> tuple[int, int]:
        for idx in range(len(self.input)):
            res = self.input[idx].find('S')
            if res > -1:
                return (res, idx) # (x, y)

    def check_neighbors(self, x, y) -> None:
        
        if y+1 > -1 and self.input[y][x] in {'|', 'J', 'L', 'S'}:
            if self.input[y-1][x] in {'|', '7', 'F'} and (x, y-1) not in self.visited:
                self.neighbors.append((x, y-1))
        if y+1 < len(self.input) and self.input[y][x] in {'|', 'F', '7', 'S'}:
            if self.input[y+1][x] in {'|', 'L', 'J'} and (x, y+1) not in self.visited:
                self.neighbors.append((x, y+1))
        if x+1 < len(self.input[0]) and self.input[y][x] in {'-', 'L', 'F', 'S'}:
            if self.input[y][x+1] in {'-', '7', 'J'} and (x+1, y) not in self.visited:
                self.neighbors.append((x+1, y))
        if x > -1 and self.input[y][x] in {'-', '7', 'J', 'S'}:
            if self.input[y][x-1] in {'-', 'L', 'F'} and (x-1, y) not in self.visited:
                self.neighbors.append((x-1, y))

    def move(self) -> None:
        steps = 1
        x, y = self.find_start()
        cx, cy = x, y

        self.check_neighbors(cx, cy)

        while len(self.neighbors) > 0:
            cx, cy = self.neighbors.pop()
            self.visited.add((cx, cy))
            steps += 1
            self.check_neighbors(cx, cy)
        
        return steps // 2
            
if __name__ == '__main__':
    x = PipeMaze(os.getcwd() + "\\input\\10.txt")