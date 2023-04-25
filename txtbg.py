#!/usr/bin/env python3.10

import random

# create the dictionary containing the field on the board.
# 0 is homebase for red/white and 25 is the homebase for black
board = {i: "" for i in range(26)}
# add the bar to the dictionary
board["bar"] = ""
# place pieces
board[1] = "R2"
board[24] = "B2"
board[19] = "R5"
board[6] = "B5"
board[17] = "R3"
board[8] = "B3"
board[12] = "R5"
board[13] = "B5"


def throw_dice(first_throw=False):
    a, b = random.randint(1, 6), random.randint(1, 6)
    if first_throw == True:
        return a, b
    else:
        if a > b:
            return str(a) + str(b)
        elif b > a:
            return str(b) + str(a)
        else:  # a double throw returns the value 4 times
            return str(a) * 4


def choose_starting_player():
    red, black = 1, 1
    while red == black:
        red, black = throw_dice(first_throw=True)
    if red > black:
        return "R", red, black
    elif black > red:
        return "B", red, black


# create variable for current turn and set it based on a dice roll between 2d6. Get the result of the dice throw and store it in variables to get the first dice result
current_player, red, black = choose_starting_player()

# order the initial throw (values in red and black):
if red > black:
    current_dice = str(red) + str(black)
elif black > red:
    current_dice = str(black) + str(red)
else:
    current_player, red, black = choose_starting_player()


def print_board():
    for i in range(13, 19):
        print(f"{i:<3}|", end="")
    print("<||||>", end="")
    for i in range(19, 25):
        print(f"{i:<3}|", end="")
    print("")
    for i in range(13, 19):
        print(f"{board[i]:<3}|", end="")
    print("<||||>", end="")
    for i in range(19, 25):
        print(f"{board[i]:<3}|", end="")
    print("")
    print("~" * 54)
    print("~" * 25 + "BAR" + "~" * 26)
    bar_value = (
        str(board["bar"]).center(54, "~")
        if board["bar"] != ""
        else "XXX".center(54, "~")
    )
    print(bar_value)
    print("~" * 54)
    for i in range(12, 6, -1):
        print(f"{i:<3}|", end="")
    print("<||||>", end="")
    for i in range(6, 0, -1):
        print(f"{i:<3}|", end="")
    print("")
    for i in range(12, 6, -1):
        print(f"{board[i]:<3}|", end="")
    print("<||||>", end="")
    for i in range(6, 0, -1):
        print(f"{board[i]:<3}|", end="")
