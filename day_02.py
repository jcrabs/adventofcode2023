"""
https://adventofcode.com/2023/day/2
"""

file = open("day_02_input.txt", "r")

data = file.readlines()

#part 1:

real_red = 12
real_green = 13
real_blue = 14

ID_sum = 0

for line in data:
    red_seen = 0
    green_seen = 0
    blue_seen = 0
    valid_game = True
    draws = line.split(";")
    for current_draw in draws:
        if current_draw.find("red") != -1:
            red_seen = int(current_draw[current_draw.find("red")-3]+current_draw[current_draw.find("red")-2])
            if red_seen > real_red:
                    valid_game = False
        if current_draw.find("green") != -1:
            green_seen = int(current_draw[current_draw.find("green")-3]+current_draw[current_draw.find("green")-2])
            if green_seen > real_green:
                    valid_game = False
        if current_draw.find("blue") != -1:
            blue_seen = int(current_draw[current_draw.find("blue")-3]+current_draw[current_draw.find("blue")-2])
            if blue_seen > real_blue:
                    valid_game = False
    if valid_game:
        game_ID = line.split(":")
        ID_sum += int(game_ID[0].removeprefix("Game "))

print(ID_sum)


#part2:

powersum = 0

for line in data:
    max_red = 0
    max_green = 0
    max_blue = 0
    draws = line.split(";")
    for current_draw in draws:
        if current_draw.find("red") != -1:
            current_red = int(current_draw[current_draw.find("red")-3]+current_draw[current_draw.find("red")-2])
            if max_red < current_red:
                max_red = current_red
        if current_draw.find("green") != -1:
            current_green = int(current_draw[current_draw.find("green")-3]+current_draw[current_draw.find("green")-2])
            if max_green < current_green:
                max_green = current_green
        if current_draw.find("blue") != -1:
            current_blue = int(current_draw[current_draw.find("blue")-3]+current_draw[current_draw.find("blue")-2])
            if max_blue < current_blue:
                max_blue = current_blue
    powersum += max_red * max_green * max_blue

print(powersum)

