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


def choose_starting_player():
    red, black = 1, 1
    while red == black:
        red, black = random.randint(1, 6), random.randint(1, 6)
    if red > black:
        return "R", red, black
    elif black > red:
        return "B", red, black


def order_dice_throw(i, j):
    if i > j:
        return str(i) + str(j)
    elif j > i:
        return str(j) + str(i)
    else:  # a double throw returns the value 4 times
        return str(i) * 4


# create variable for current turn and set it based on a dice roll between 2d6. Get the result of the dice throw and store it in variables to get the first dice result
current_player, red, black = choose_starting_player()

# order the initial throw (values in red and black):
current_dice = order_dice_throw(red, black)


def print_board():
    for key, value in board.items():
        if type(key) == int:
            if key <= 24 and key >= 19:
                print(str(key) + " | ")
                print("---")
                print(value + " | ")
            if key <= 18 and key >= 13:
                print(str(key) + " | ")
                print("---")
                print(value + " | ")
            if key == 25:
                print("HOME")
                print("---")
                print(value)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~ BAR: " + board["bar"] + "~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for key, value in board.items():
        if type(key) == int:
            if key <= 12 and key >= 7:
                print(str(key) + " | ")
                print("---")
                print(value + " | ")
            if key <= 6 and key <= 1:
                print(str(key) + " | ")
                print("---")
                print(value + " | ")
            if key == 0:
                print("HOME")
                print("---")
                print(value)
