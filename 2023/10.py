'''

--- Advent of Code 2023 ---

Day 10: Pipe Maze
https://adventofcode.com/2023/day/10

'''

from collections import deque, defaultdict

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
    def count_steps(self) -> int:
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

    # This changes the starting tile to a proper pipe as the
    # old value of the starting position is 'S'. This is required
    # for the counting of the tiles that are inside the loop.
    def change_start(self) -> None:
        x, y = self.find_start_coords()
        neighbors = self.find_start_neighbors(x, y)
        start_offsets = []

        for cx, cy in neighbors:
            start_offsets.append((cx - x, cy - y))
        for pipe, offset in self.PIPES_OFFSET.items():
            # We use this scuffed if-statement because we need to check
            # what the pipe is with the offset, but the problem is that
            # my start_offset can have different positions than the
            # constant dictionary PIPES_OFFSET,
            if tuple(start_offsets) == (offset[0], offset[1]) or tuple(start_offsets) == (offset[1], [0]):
                self.input[y][x] = pipe

    # We can count the tiles inside of the loop by using the Ray-tracing algorithm or
    # also known as the Even-Odd Rule algorithm. We count how many sides we have passed
    # by and check if it's odd or even. If it's odd, that means the tile is inside and
    # if it's even, that means the tile is outside. We don't count '-' as it is collinear
    # with the pipes that we have passed through; we also don't count F--7 and L--J as
    # they don't vertically cross the row, they go to different vertical rows.
    def count_inside(self) -> int:
        count = 0
        pipes = defaultdict(lambda: (140, 0))

        x, y = self.find_start_coords()
        neighbors = self.find_start_neighbors(x, y)
        visited = set({(x, y)})
        self.change_start()

        while len(neighbors) > 0:
            x, y = neighbors.pop()
            visited.add((x, y))
            pipes[y] = (min(pipes[y][0], x), max(pipes[y][1], x))
            self.check_connections(x, y, neighbors, visited)

        for y, x_range in pipes.items():
            cross = 0
            start = ''
            for x in range(x_range[0], x_range[1]):
                tile = self.input[y][x]
                if (x, y) not in visited:
                    if cross % 2 == 1:
                        count += 1
                else:
                    match tile:
                        case 'F':
                            start = 'F'
                        case 'L':
                            start = 'L'
                        case '|':
                            cross += 1
                        case 'J':
                            if start == 'F':
                                cross += 1
                                start = ''
                        case '7':
                            if start == 'L':
                                cross += 1
                                start = ''

        return count