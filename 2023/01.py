'''

--- Advent of Code 2023 ---

Day 01: Trebuchet?!
https://adventofcode.com/2023/day/1

'''

import string

class Trebuchet:
    
    # Initialize the string to value.
    # We add the first and last letters of the words for combined
    # string values such us 'oneight'.
    stringNumbers = dict({
        'one':   'o1e',
        'two':   't2o',
        'three': 't3e',
        'four':  'f4r',
        'five':  'f5e',
        'six':   's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine':  'n9e'
    })
    
    def __init__(self, input: str) -> None:
        self.input = open(input).read().splitlines()
        
    def number_calibration(self) -> int:
        
        # Initialize the sum of all of the calibration values.
        calib_val = 0
        
        for line in self.input:
            # Remove all the characters in the string. Keep only the integers
            # because we only need the digits.
            line = line.translate({ord(i): "" for i in string.ascii_lowercase})
            calib_val += int(line[0] + line[len(line) - 1])
        
        return calib_val

    def string_calibration(self) -> int:
        
        # Initialize the sum of all of the calibration values.
        calib_val = 0
        
        for line in self.input:
            
            # Replace the string values into actual values.
            for old, new in self.stringNumbers.items():
                line = line.replace(old, new)
            
            # Remove all the characters in the string. Keep only the integers
            # because we only need the digits.
            line = line.translate({ord(i): "" for i in string.ascii_lowercase})
            calib_val += int(line[0] + line[len(line) - 1])
            
        return calib_val