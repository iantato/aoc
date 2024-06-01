'''

--- Advent of Code 2023 ---

Day 08: Haunted Wasteland
https://adventofcode.com/2023/day/8

'''

from functools import reduce
from math import lcm

class Directions:
    
    def __init__(self, data: str) -> None:
        input = open(data).read().splitlines()
        self.directions = input[0]
        self.nodes = {}
        
        raw_nodes = input[2:]
        for node in raw_nodes:
            node, network = node.split(" = ")
            left, right = network[1:-1].split(", ")
            self.nodes[node] = (left, right)
        
    def check_node(self, direction: int, node: str) -> str:
        
        return self.nodes.get(node)[direction]
    
    def count_steps(self) -> int:
        
        node = "AAA"
        step = 0
        
        while node != 'ZZZ':
            for direction in self.directions:
                
                node = self.check_node(0 if direction == 'L' else 1, node)
                step += 1
                
        return step
    
    def check_all(self) -> None:
        
        nodes = {key: node for key, node in self.nodes.items() if key[-1] == 'A'}
        new_nodes = []
        step_count = 0
        steps = []
        
        cond = len(nodes)
        while len(steps) < cond:
            for direction in self.directions:
                for i in nodes.keys():
                    node = self.check_node(0 if direction == 'L' else 1, i)
                    if node[-1] == 'Z':
                        steps.append(step_count + 1)
                    else:
                        new_nodes.append(node)
                        
                nodes = {key: node for key, node in self.nodes.items() if key in new_nodes}
                new_nodes = []
                step_count += 1
        
        return reduce(lcm, steps)