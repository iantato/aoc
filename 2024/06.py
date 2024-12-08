'''

--- Advent of Code 2024 ---
Day 06: Guard Gallivant

https://adventofcode.com/2024/day/6

'''

class GuardMap:

    MOVES = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def __init__(self, dir: str, looping: bool = False) -> None:
        with open(dir) as f:
            self.guard_map = f.read().splitlines()

    def __repr__(self) -> str:
        if self.looping:
            return str(self.obstacle_loop_test(self.guard_map))
        return str(self.move_guard(self.guard_map, *self.find_guard(self.guard_map)))

    def find_guard(self, map: list[str]) -> None:
        for idy, line in enumerate(map):
            if line.find('^') > -1:
                return (idy, line.find('^'))

    def move_guard(self, map: list[str], idy: int, idx: int) -> int:
        visited = set({(idy, idx)})
        move = 0

        while True:
            ay, ax = self.MOVES[move]
            if idy + ay not in range(len(map)) or idx + ax not in range(len(map[0])):
                break
            if map[idy + ay][idx + ax] == '#':
                move = (move + 1) % 4
                ay, ax = self.MOVES[move]

            idy += ay
            idx += ax

            visited.add((idy, idx))

        return len(visited)

    def check_obstacles(self, map: list[str], idy: int, idx: int) -> int:
        visited_obstacles = set()
        move = 0

        while True:
            ay, ax = self.MOVES[move]
            if idy + ay not in range(len(map)) or idx + ax not in range(len(map[0])):
                return 0
            if ((idy + ay, idx + ax), move) in visited_obstacles:
                return 1
            visited_obstacles.add(((idy, idx), move))

            if map[idy + ay][idx + ax] == '#':
                move = (move + 1) % 4
                ay, ax = self.MOVES[move]
                continue

            idy += ay
            idx += ax

    def obstacle_loop_test(self, map: list[str]) -> int:
        loops = 0

        for y in range(len(map)):
            for x in range(len(map[0])):
                test_map = map.copy()
                row = list(test_map[y])
                if row[x] == '^' or row[x] == '#':
                    continue
                row[x] = '#'
                test_map[y] = ''.join(row)

                loops += self.check_obstacles(test_map, *self.find_guard(test_map))

        return loops