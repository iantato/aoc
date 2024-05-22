'''

--- Advent of Code 2023 ---

Day 02: Cube Conundrum
https://adventofcode.com/2023/day/2

'''

import re

class Cube:
    
    def __init__(self, input: str) -> None:
        self.input = open(input).read().splitlines()
    
    # Uses integer arguments r, b, g to set how many 
    # cubes the bag contains for each color.
    def check_possibility(self, r: int, b: int, g: int) -> int:
        
        # Initialize the sum of the possible Game IDs
        total_id = 0
        
        for i in self.input:
            # Uses RegEx to split the string with multiple delimiters which are:
            # ";" "," ": "
            results = re.split("; |, |:\s", i)
            # Initialize the check if the game is possible.
            possible = True
            
            for cube in results[1:]:
                number, color = cube.split(' ')
                
                # Check if the cube number is larger than the amount of
                # cube placed inside the bag. If it is, the game is not
                # possible. Otherwise, we add the Game ID to the sum.
                match (color):
                    
                    case 'red': 
                        if int(number) > r:
                            possible = False
                    case 'blue': 
                        if int(number) > b:
                            possible = False
                    case 'green': 
                        if int(number) > g:
                            possible = False
            
            if possible: 
                total_id += int(results[0].split(' ')[1])
                
        return total_id
    
    def lowest_cubes(self) -> int:
        
        # Initialize the sum of the power of a set of cubes.
        total_cube = 0
        
        for i in self.input:
            # Uses RegEx to split the string with multiple delimiters which are:
            # ";" "," ": "
            results = re.split("; |, |:\s", i)
            # Initialize the dictionary for maximum cubes amount.
            cubes = dict({
                'red' : 0,
                'blue': 0,
                'green': 0
            })
            
            # Set the cubes' colors to the max number in the dictionary.
            # Add the power of the set of cubes to the sum.
            for cube in results[1:]:
                number, color = cube.split(' ')
                
                match (color):
                    
                    case 'red': 
                        if int(number) > cubes['red']:
                            cubes['red'] = int(number)
                    case 'blue': 
                        if int(number) > cubes['blue']:
                            cubes['blue'] = int(number)
                    case 'green': 
                        if int(number) > cubes['green']:
                            cubes['green'] = int(number)
            
            total_cube += cubes['red'] * cubes['blue'] * cubes['green']
        
        return total_cube