'''

--- Advent of Code 2023 ---

Day 06: Camel Cards
https://adventofcode.com/2023/day/7

'''

from collections import Counter
from functools import cmp_to_key

class CamelCards:
    
    strength = "23456789TJQKA"
    
    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()
    
    # Compare which of the hand has a stronger hand type.
    # Returning 1 enables it to move further in the list when
    # used as a key by sorted().
    # We use most_common() here because the hand with
    # the largest first element will equal to a stronger
    # hand type. 
    def compare_types(self, hand1: tuple, hand2: tuple) -> int:
        
        hand1 = Counter(hand1[0]).most_common()
        hand2 = Counter(hand2[0]).most_common()
        
        for i in range(min(len(hand1), len(hand2))):
            if hand1[i][1] > hand2[i][1]:
                return 1
            elif hand1[i][1] < hand2[i][1]:
                return -1
            
        return 0
    
    # Compare each cards of the hands with the given card
    # strengths. This is used when the hands have the same
    # hand type.
    def compare_card(self, hand1: tuple, hand2: tuple) -> int:
        
        if self.compare_types(hand1, hand2) != 0:
            return self.compare_types(hand1, hand2)
        
        for i in range(0, 5):
            if self.strength.index(hand1[0][i]) > self.strength.index(hand2[0][i]):
                return 1
            elif self.strength.index(hand1[0][i]) < self.strength.index(hand2[0][i]):
                return -1
        
        return 0
    
    # Using the Counter from collections, we generate a dictionary
    # without the J card so that we can get the most common card
    # in the hand. The most common card will of course have the largest
    # value which is why we use max() with key of dict.get.
    def check_wildcard(self, hand: tuple) -> tuple:
        
        if hand[0] == 'JJJJJ':
            return hand
        
        c_hand = Counter(x for x in hand[0] if x != 'J')
        return (hand[0].replace('J', max(c_hand, key=c_hand.get)), hand[1])
    
    def type_with_wildcard(self, hand1: tuple, hand2: tuple) -> int:
        
        hand1 = Counter(self.check_wildcard(hand1)[0]).most_common()
        hand2 = Counter(self.check_wildcard(hand2)[0]).most_common()
        
        for i in range(min(len(hand1), len(hand2))):
            if hand1[i][1] > hand2[i][1]:
                return 1
            elif hand1[i][1] < hand2[i][1]:
                return -1
            
        return 0
    
    def compare_with_wildcard(self, hand1: tuple, hand2: tuple) -> int:
        
        if self.type_with_wildcard(hand1, hand2) != 0:
            return self.type_with_wildcard(hand1, hand2)
        
        for i in range(0, 5):
            if self.strength.index(hand1[0][i]) > self.strength.index(hand2[0][i]):
                return 1
            elif self.strength.index(hand1[0][i]) < self.strength.index(hand2[0][i]):
                return -1
        
        return 0
    
    def total(self) -> int:
        
        total = 0
        
        # Convert the inputs into a readable format for the program.
        hands = [tuple(i.split(" ")) for i in self.input]
        # Sort the hands using the compare_card function.
        hands = sorted(hands, key = cmp_to_key(self.compare_card))
        
        for i in range(len(hands)):
            bid = hands[i][1]
            total += int(bid) * (i + 1)
        
        return total
    
    def total_wildcard(self) -> None:
        
        self.strength = "J23456789TQKA"
        total = 0
        
        hands = [tuple(i.split(" ")) for i in self.input]
        hands = sorted(hands, key = cmp_to_key(self.compare_with_wildcard))
        
        for i in range(len(hands)):
            bid = hands[i][1]
            total += int(bid) * (i + 1)
        
        return total