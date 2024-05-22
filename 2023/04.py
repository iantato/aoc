'''

--- Advent of Code 2023 ---

Day 04: Scratch Cards
https://adventofcode.com/2023/day/4

'''

class Scratchcards:
    
    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()
    
    # Parse the cards into a list of numbers instead of having the list as
    # a list of strings. This creates a list of separated numbers:
    # The winning numbers and the player's numbers.
    def parse_cards(self) -> list:
        
        parsed_cards = list([i.split("|") for i in self.input])
        
        for index, cards in enumerate(parsed_cards):
            parsed_cards[index] = list([
                list(map(int, filter(None, parsed_cards[index][0].split(":")[1].split(" ")))),
                list(map(int, filter(None, parsed_cards[index][1].split(" "))))
            ])
        
        return parsed_cards
    
    def total_points(self) -> int:
        
        # Initialize the parsed cards list and the total sum of the points.
        parsed_cards = self.parse_cards()
        total = 0
        
        # Check if the player's number are in the winning number and multiplies
        # them by two for each iteration.
        for winning, player in parsed_cards:
            points = 0
            for num in player:
                if num in winning:
                    match points:
                        case 0:
                            points += 1
                        case _:
                            points *= 2
        
            total += points

        return total

    def dupe_cards(self) -> int:
        
        # Initialize the parsed cards list and creates a dictionary of the
        # number of copies of each cards. We initialize the number of copies
        # to one as we have one original copies of each cards.
        parsed_cards = self.parse_cards()
        cards = dict({i:1 for i in range(len(parsed_cards))})
        
        for index in range(len(parsed_cards)):
            # Count how many numbers are winning.
            winning, player = parsed_cards[index]
            winning = len(list(filter(None, [i in winning for i in player])))
            
            # We distribute the copies of cards. We multiply
            # how many we are distributing by the amount of
            # the copies we have of the current card.
            for i in range(index + 1, index + winning + 1):
                cards[i] += 1 * cards.get(index)
        
        return sum(cards.values())