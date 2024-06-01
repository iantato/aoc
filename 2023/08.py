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
        
        # This initializes the nodes and where they connect to 
        # into a dictionary so that we can easily access them.
        raw_nodes = input[2:]
        for node in raw_nodes:
            node, network = node.split(" = ")
            left, right = network[1:-1].split(", ")
            self.nodes[node] = (left, right)
    
    # Check where the node connects to and return the connection.
    # In this function, the direction must already be converted
    # into an integer, L = 0, and R = 0. This is where our
    # node connection dictionary gets used.
    def check_node(self, direction: int, node: str) -> str:
        return self.nodes.get(node)[direction]
    
    # Start with the node 'AAA' and check how many steps we need to
    # get to 'ZZZ' using the L & R directions we were given.
    def count_steps(self) -> int:
        
        node = "AAA"
        step = 0
        
        while node != 'ZZZ':
            for direction in self.directions:
                
                node = self.check_node(0 if direction == 'L' else 1, node)
                step += 1
                
        return step
    
    # We start with multiple nodes in this one-Any node that ends with
    # an 'A' in the end. We don't want to compute in parallel or in
    # threading hence instead we're going to find the LCM.
    def check_all(self) -> None:
        
        nodes = {key: node for key, node in self.nodes.items() if key[-1] == 'A'}
        new_nodes = []
        step_count = 0
        steps = []
        
        # Stop the loop when all the paths have been calculated. We can
        # determine that we have got all the paths' calculated when the
        # steps array is larger than our original node count which in my
        # input's case: 6.
        cond = len(nodes)
        while len(steps) < cond:
            for direction in self.directions:
                for i in nodes.keys():
                    node = self.check_node(0 if direction == 'L' else 1, i)
                    
                    # If the node ends with a 'Z', we add the steps count
                    # to the array with a +1 because we haven't registered
                    # the step we have took to get to the 'Z' yet.
                    # This ends with us not adding the node that ends with
                    # 'Z" in the new_nodes variable because we already
                    # have calculated it and we don't need to anymore.
                    if node[-1] == 'Z':
                        steps.append(step_count + 1)
                    else:
                        new_nodes.append(node)
                        
                nodes = {key: node for key, node in self.nodes.items() if key in new_nodes}
                new_nodes = []
                step_count += 1
        
        return reduce(lcm, steps)