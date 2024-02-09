"""
https://adventofcode.com/2023/day/4
"""

import pathlib
input_lines = pathlib.Path("day_04_input.txt").read_text().splitlines()

cards = []

for line in input_lines:
    _, _, raw_card = line.partition(":")
    numbers_win, _, numbers_have = raw_card.partition("|")
    numbers_win = numbers_win.split()
    numbers_have = numbers_have.split()
    cards.append((numbers_win,numbers_have))

#part 1 ----------------------------------------------------------------------------------

total_points = 0

for card in cards:
    points_per_card = 0
    for number in card[0]:        
        if number in card[1]:        
            if points_per_card == 0:
                points_per_card += 1
            elif points_per_card > 0:
                points_per_card = points_per_card*2
    total_points += points_per_card
    
print(total_points)

#part 2 ----------------------------------------------------------------------------------

instances_per_card = [1] * len(cards)
matches_per_card = [0] * len(cards)

for i in range(len(cards)):
    for number in cards[i][0]:
        if number in cards[i][1]:
            matches_per_card[i] += 1
    for j in range(matches_per_card[i]):
        if i+j+1 > len(cards):
            break
        instances_per_card[i+j+1] += instances_per_card[i]

print(sum(instances_per_card))
