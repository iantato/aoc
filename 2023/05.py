'''

--- Advent of Code 2023 ---

Day 05: If You Give A Seed A Fertilizer
https://adventofcode.com/2023/day/5

'''

class Garden:
    
    def __init__(self, data: str) -> None:
        self.input = open(data).read().split('\n\n')
    
    # Get the seeds' list from the first line.
    def get_seeds(self) -> list:
        return map(int, self.input[0].split(" ")[1:])
    
    # Convert the seeds' list into ranges.
    def get_ranges(self) -> list:
        raw_seeds = list(self.get_seeds())
        ranged_seeds = list([])

        for i in range(0, len(raw_seeds), 2):
            ranged_seeds.append([raw_seeds[0], sum(raw_seeds[:2])])
            del raw_seeds[:2]
        
        return ranged_seeds
    
    def get_lowest_loc(self, seeds: list) -> int:
        
        locations = list([])

        for seed in seeds:
            check = seed

            for i in self.input[1:]:
                
                mapping = i.split("\n")[1:]
                
                # Faster solution is to get the map e.g seed-to-soil map: 52 50 48
                # then to minus the dest to src (50 - 52 = -2) and then minus the offset (-2)
                # to the seed (79 - -2 = 81) which converts it.
                for j in mapping:
                    mapped, start_index, length = map(int, j.split(" "))
                    
                    if start_index <= check < start_index + length:
                        converted = (start_index + length - 1) - check
                        converted = (mapped + length - 1) - converted
                        check = converted
                        break
            
            locations.append(check)
        
        return min(locations)

    def ranged_lowest_loc(self) -> int:

        seeds = self.get_ranges()
        locations = []
        
        # Brute-force check all the numbers in each range.
        for start, end in seeds:
            locations.append(self.get_lowest_loc(list(range(start, end + 1))))
        
        return min(locations)