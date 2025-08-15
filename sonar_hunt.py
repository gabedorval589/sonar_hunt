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


    
def draw_board(board):
    """Draw the board data structure."""
    tensDigitsLine = '    ' # Initial space for the numbers down the left side of the board
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # Print the numbers across the top of the board.
    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()

    # Print each of the 15 rows.
    for row in range(15):
        # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        # Create the string for this row on the board.
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    # Print the numbers across the bottom of the board.
    print()
    print('   ' + ('0123456789' * 6))
    print(tensDigitsLine)

    
def get_random_chests(num_chests):
    """ Create a list of chest data structures (two-item lists of x, y int coordinates)."""
    chests = []
    while len(chests) < num_chests:
        new_chest = [random.randint(0, 59), random.randint(0, 14)]
        if new_chest not in chests: # Make sure a chest is not already here.
            chests.append(new_chest)
    return chests
