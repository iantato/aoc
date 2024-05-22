'''

--- Advent of Code 2023 ---

Day 06: Wait For It
https://adventofcode.com/2023/day/6

'''

import math
import os

class Errors:
    
    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()
    
    def organize_input(self, data: list) -> list:
        
        # Turn the data into a 2D array where we have a
        # pair of time and distance as an integer.
        time = data[0].split()[1:]
        dist = data[1].split()[1:]
        
        return [(int(time[i]), int(dist[i])) for i in range(len(time))]

    def combine_input(self, data: list) -> list:
        
        time = data[0].split()[1:]
        dist = data[1].split()[1:]
        
        return [(int("".join(time)), int("".join(dist)))]
    
    def calc_margin_error(self, races: list) -> int:
    
        results = list([])
        ways = 0
        
        # We find the difference of the number of milliseconds the 
        # button has been pressed with the total time of the race.
        # We multiply it to the amount of milliseconds the button
        # was held for because the boat travels: 
        # {0+1ms of button pressed/ms}
        for time, dist in races:

            for pressed in range(time - 1, 1, -1):
                
                traveled = (time - pressed) * pressed
                if traveled > dist:
                    ways += 1
            
            results.append(ways)
            ways = 0
    
        return math.prod(results)
        
        
        
x = Errors(os.getcwd() + "\\input\\06.txt")
print(x.calc_margin_error(x.combine_input(x.input)))