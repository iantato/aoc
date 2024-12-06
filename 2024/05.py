'''

--- Advent of Code 2024 ---

Day 05: Print Queue
https://adventofcode.com/2024/day/5

'''

from collections import defaultdict

class PageOrder:

    def __init__(self, dir: str, sorted: bool = True) -> None:
        self.sorted = sorted

        with open(dir) as f:
            raw_data = f.read().splitlines()

            self.rules = raw_data[:raw_data.index('')]
            self.updates = raw_data[raw_data.index('') + 1:]

    def __repr__(self) -> str:
        if self.sorted:
            middle = self.sorted_pages(self.rules)
        else:
            middle = self.unsorted_pages(self.rules)

        return str(middle)

    def get_rules_order(self, rules: list[str]) -> defaultdict:
        rules_order = defaultdict(set)

        for rule in rules:
            key, value = rule.split('|')
            if value is None:
                rules[int(key)]
            else:
                rules_order[int(key)].add(int(value))

        return rules_order

    def order_pages(self, pages: list[int], rules_order: dict[int: list[int]]) -> list[int]:
        for main_idx in range(len(pages)):
            for current in range(len(pages)):
                if pages[main_idx] not in rules_order[pages[current]]:
                    temp = pages[main_idx]
                    pages[main_idx] = pages[current]
                    pages[current] = temp

        return pages

    def sorted_pages(self, rules: list[str]) -> int:
        middle = 0
        rules_order = self.get_rules_order(rules)

        for updates in self.updates:
            updates = list(map(int, updates.split(',')))
            for i in range(len(updates)):
                if not all(j not in rules_order[updates[i]] for j in updates[:i]):
                    break
            else:
                middle += updates[len(updates) // 2]

        return middle

    def unsorted_pages(self, rules: list[str]) -> None:
        middle = 0
        rules_order = self.get_rules_order(rules)

        for updates in self.updates:
            updates = list(map(int, updates.split(',')))
            for i in range(len(updates)):
                if not all(j not in rules_order[updates[i]] for j in updates[:i]):
                    updates = self.order_pages(updates, rules_order)
                    middle += updates[len(updates) // 2]

                    break

        return middle



if __name__ == '__main__':
    import os
    print(PageOrder(os.getcwd() + '/input/05.txt', False))