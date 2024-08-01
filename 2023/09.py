'''

--- Advent of Code 2023 ---

Day 09: Mirage Maintenance
https://adventofcode.com/2023/day/9

'''

class OasisSensor:
    
    def __init__(self, data: str) -> None:
        self.input = [list(map(int, i.split(" "))) for i in open(data).read().splitlines()]
    
    # Find the difference in a sequence and generate it as a list.
    def find_difference(self, val: list[int]) -> list[int]:
        return [val[i + 1] - val[i] for i in range(len(val) - 1)]
    
    # Generate all the levels of differences in all
    # the sequences until the difference hits 0.
    def generate_history(self, data: list[int]) -> list[int]:
        
        all_history = []
        
        for i in data:
            history = [i]
            differences = i
            while not all(j == 0 for j in differences):
                differences = self.find_difference(differences)
                history += [differences]
            
            all_history += [history]
        
        return all_history
    
    # Find the next element in the original list by getting
    # all the last elements of the histories we generated and
    # summing them up.
    def find_next(self) -> int:
        
        total = 0
        
        for diff in self.generate_history(self.input):
            total += sum([i[-1] for i in diff[::-1][1:]])
            
        return total
    
    # To find the previous element, we just subtract all the
    # first elements together of the histories
    # that we generated.
    def find_previous(self) -> int:
        
        total = 0
        
        for diff in self.generate_history(self.input):
            start = [i[0] for i in diff[::-1][1:]]
            current_val = 0
            
            for i in start:
                current_val = i - current_val
            
            total += current_val
        
        return total