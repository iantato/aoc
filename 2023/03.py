'''

--- Advent of Code 2023 ---

Day 03: Gear Ratios
https://adventofcode.com/2023/day/3

'''

class Gondola:
    
    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()
    
    # These functions uses recursion in order to find the full
    # numbers from a single digit.
    # Uses a list for the number buffer so that we're able to use the
    # reverse function when we're checking the left decimals.
    # It returns a string which will be converted into an integer later on.
    def check_decimal_right(self, row: int, index: int, number_buffer: list) -> str:
        if index <= len(self.input[row]) - 1:
            if self.input[row][index].isdigit():
                number_buffer.append(self.input[row][index])
                return self.check_decimal_right(row, index + 1, number_buffer)
            else:
                return ''.join(number_buffer)
        else:
            return ''.join(number_buffer)
    
    def check_decimal_left(self, row: int, index: int, number_buffer: list) -> str:
        if self.input[row][index].isdigit() and index >= 0:
            number_buffer.append(self.input[row][index])
            return self.check_decimal_left(row, index - 1, number_buffer)
        else:
            number_buffer.reverse()
            return ''.join(number_buffer)
    
    def get_gears(self) -> int:
        
        # Initialize the gear's sum.
        out = 0
        
        # Loop through the multi-dimensional array and use the row's index
        # along with the character's indexes in order to loop through.
        for row, line in enumerate(self.input):
            for index, char in enumerate(line):
                # Check if the current character is a symbol.
                if not char.isdigit() and char != '.':
                    # Initialize variables to check whether a decimal
                    # is above/below a symbol so that we don't have to check
                    # the diagonals because the diagonals may be a part
                    # of the digit.
                    above_isdigit = False
                    below_isdigit = False
                    
                    # Check the digit above the current symbol.
                    if row - 1 >= 0:
                        if self.input[row - 1][index].isdigit():
                            num = (self.check_decimal_left(row - 1, index, list([])) + 
                                   self.check_decimal_right(row - 1, index + 1, list([])))
                            above_isdigit = True
                            out += int(num)
                            
                    # Check the digit below the current symbol.
                    if row + 1 <= len(self.input) - 1:
                        if self.input[row + 1][index].isdigit():
                            num = (self.check_decimal_left(row + 1, index, list([])) +
                                   self.check_decimal_right(row + 1, index + 1, list([])))
                            below_isdigit = True
                            out += int(num)
                    
                    # Check the digit directly to the left of the symbol.
                    if index - 1 >= 0:
                        if self.input[row][index - 1].isdigit():
                            num = self.check_decimal_left(row, index - 1, list([]))
                            out += int(num)
                    
                    # Check the digit directly to the right of the symbol.
                    if index + 1 <= len(self.input[row]) - 1:
                        if self.input[row][index + 1].isdigit():
                            num = self.check_decimal_right(row, index + 1, list([]))
                            out += int(num)
                            
                    # Check the diagonals only when there are no digits above.
                    if not above_isdigit:
                        # Check the digit to the upper left of the symbol.
                        if row - 1 >= 0 and index - 1 >= 0:
                            if self.input[row - 1][index - 1].isdigit():
                                num = self.check_decimal_left(row - 1, index - 1, list([]))
                                out += int(num)

                        # Check the digit to the upper right of the symbol.
                        if row - 1 >= 0 and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row - 1][index + 1].isdigit():
                                num = self.check_decimal_right(row - 1, index + 1, list([]))
                                out += int(num)
                                
                    # Check the diagonals only when there are no digits below.
                    if not below_isdigit:
                        # Check the digit to the lower left of the symbol.
                        if row + 1 <= len(self.input) - 1 and index - 1 >= 0:
                            if self.input[row + 1][index - 1].isdigit():
                                num = self.check_decimal_left(row + 1, index - 1, list([]))
                                out += int(num)
                        
                        # Check the digit to the lower right of the symbol.
                        if row + 1 <= len(self.input) and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row + 1][index + 1].isdigit():
                                num = self.check_decimal_right(row + 1, index + 1, list([]))
                                out += int(num)
                    
        return out
    
    def gear_ratio(self) -> int:
        
        out = 0
        
        # Uses same loop as the get_gears function. Instead of adding the sum
        # into the output variable immediately, we first check if there are two
        # numbers that are adjacent to the * symbol and then multiply them to get
        # the output.
        for row, line in enumerate(self.input):
            for index, char in enumerate(line):
                
                # Conditional statement for finding the * symbols.
                if char == '*':
                    gears = list([])
                    above_isdigit = False
                    below_isdigit = False
                    
                    # Check upper row.
                    if row - 1 >= 0:
                        if self.input[row - 1][index].isdigit():
                            num = (self.check_decimal_left(row - 1, index, list([])) + 
                                   self.check_decimal_right(row - 1, index + 1, list([])))
                            above_isdigit = True
                            gears.append(int(num))
                            
                    # Check lower row.
                    if row + 1 <= len(self.input) - 1:
                        if self.input[row + 1][index].isdigit():
                            num = (self.check_decimal_left(row + 1, index, list([])) +
                                   self.check_decimal_right(row + 1, index + 1, list([])))
                            below_isdigit = True
                            gears.append(int(num))
                    
                    # Check left.
                    if index - 1 >= 0:
                        if self.input[row][index - 1].isdigit():
                            num = self.check_decimal_left(row, index - 1, list([]))
                            gears.append(int(num))
                    
                    # Check right.
                    if index + 1 <= len(self.input[row]) - 1:
                        if self.input[row][index + 1].isdigit():
                            num = self.check_decimal_right(row, index + 1, list([]))
                            gears.append(int(num))
                            
                    ## Check diagonals
                    # Check upper.
                    if not above_isdigit:
                        if row - 1 >= 0 and index - 1 >= 0:
                            if self.input[row - 1][index - 1].isdigit():
                                num = self.check_decimal_left(row - 1, index - 1, list([]))
                                gears.append(int(num))

                        if row - 1 >= 0 and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row - 1][index + 1].isdigit():
                                num = self.check_decimal_right(row - 1, index + 1, list([]))
                                gears.append(int(num))
                                
                    # Check lower.
                    if not below_isdigit:
                        if row + 1 <= len(self.input) - 1 and index - 1 >= 0:
                            if self.input[row + 1][index - 1].isdigit():
                                num = self.check_decimal_left(row + 1, index - 1, list([]))
                                gears.append(int(num))
                        
                        if row + 1 <= len(self.input) and index + 1 <= len(self.input[row]) - 1:
                            if self.input[row + 1][index + 1].isdigit():
                                num = self.check_decimal_right(row + 1, index + 1, list([]))
                                gears.append(int(num))

                    if len(gears) == 2:
                        out += gears[0] * gears[1]
    
        return out