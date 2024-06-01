

import os
from collections import Counter
from functools import cmp_to_key

class CamelCards:
    
    strength = "23456789TJQKA"
    
    def __init__(self, data: str) -> None:
        self.input = open(data).read().splitlines()
        
    def compare_types(self, hand1: tuple, hand2: tuple) -> int:
        
        hand1 = Counter(hand1[0]).most_common()
        hand2 = Counter(hand2[0]).most_common()
        
        for i in range(min(len(hand1), len(hand2))):
            if hand1[i][1] > hand2[i][1]:
                return 1
            elif hand1[i][1] < hand2[i][1]:
                return -1
            
        return 0
    
    def compare_card(self, hand1: tuple, hand2: tuple) -> int:
        
        if self.compare_types(hand1, hand2) != 0:
            return self.compare_types(hand1, hand2)
        
        for i in range(0, 5):
            if self.strength.index(hand1[0][i]) > self.strength.index(hand2[0][i]):
                return 1
            elif self.strength.index(hand1[0][i]) < self.strength.index(hand2[0][i]):
                return -1
        
        return 0
    
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
        
        hands = [tuple(i.split(" ")) for i in self.input]
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
        
x = CamelCards(os.getcwd() + "\\input\\07.txt")

# print(x.compare_hands(("K9KKK", "100"), ("A4T7Q", "100")))
print(x.total_wildcard())