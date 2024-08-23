'''

--- Advent of Code 2023 ---

Day 10: Pipe Maze
https://adventofcode.com/2023/day/10

'''

import os
from collections import deque

class PipeMaze():

    # A constant value that lists down
    # all the offset values of the pipes
    # for easier traversal.
    # Stored in the position of:
    #  off1     off2
    # (X, Y) , (X, Y)
    PIPES_OFFSET = {
        '|': ((0, 1), (0, -1)),
        '-': ((1, 0), (-1, 0)),
        'L': ((1, 0), (0, -1)),
        'J': ((-1, 0), (0, -1)),
        '7': ((-1, 0), (0, 1)),
        'F': ((1, 0), (0, 1))
    }

    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()

    # Find where the start of the pipes are by
    # looping through the whole two-dimensional
    # array that we have made and returning the
    # (X, Y) value.
    def find_start_coords(self) -> tuple[int, int]:
        for idx in range(len(self.input)):
            res = self.input[idx].find('S')
            if res > -1:
                return (res, idx)

    # Find the possible pipes we can traverse
    # from the starting coordinates. We then
    # return the values of the neighbors with
    # a queue as we're going to be using the
    # DFS (Depth first search) algorithm.
    def find_start_neighbors(self, x: int, y: int) -> deque:
        neighbors = deque()

        if self.input[y-1][x] in {'|', '7', 'F'}:
            neighbors.append((x, y-1))
        if self.input[y+1][x] in {'|', 'L', 'J'}:
            neighbors.append((x, y+1))
        if self.input[y][x+1] in {'-', '7', 'J'}:
            neighbors.append((x+1, y))
        if self.input[y][x-1] in {'-', 'L', 'F'}:
            neighbors.append((x-1, y))

        return neighbors

    # Using the our constant values for offsets, we can
    # loop through them and check if the connected pipe/neighbor
    # has already been visited. If the pipe hasn't been visited,
    # that means we can go through it and then we add it to the
    # neighbors. DFS (Depth-first-search) algorithm used.
    def check_connections(self, x: int, y: int, neighbors: deque, visited: set) -> tuple[int, int]:
        pipes_offset = self.PIPES_OFFSET.get(self.input[y][x])

        for x_offset, y_offset in pipes_offset:
            if (x+x_offset, y+y_offset) not in visited:
                neighbors.append((x+x_offset, y+y_offset))

    # This is the main function that counts the steps of the
    # traversal of the loop. The steps is then divided by
    # 2 so that we can get the final answer for the problem.
    def count_steps(self) -> None:
        steps = 1

        x, y = self.find_start_coords()
        neighbors = self.find_start_neighbors(x, y)
        visited = set({(x, y)})

        while len(neighbors) > 0:
            x, y = neighbors.pop()
            visited.add((x, y))
            steps += 1
            self.check_connections(x, y, neighbors, visited)

        return steps // 2