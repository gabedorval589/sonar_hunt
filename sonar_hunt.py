# Sonar Treasure Hunt

import random
import sys
import math

def get_new_board():
    """ Create a new 60x15 board data structure."""
    board = []
    for x in range(60): # The main list is a list of 60 lists."""
        board.append([])
        for y in range(15): # Each list in the main list has 15 single-character strings.
            # Use different characters for the ocean to make it more readable.
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board