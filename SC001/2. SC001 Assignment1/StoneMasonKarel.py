"""
File: StoneMasonKarel.py
Name: Nancy
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (1, 1), facing East. Columns are not completely filled with beepers.
    Post-condition: Karel is at (1, y), facing East and facing a wall. Columns are completely filled with beepers
    """
    while front_is_clear():
        fill_column()
        move_to_next_column()
    fill_column()
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def fill_column():
    """
    Pre-condition: Karel is on Street 1, facing East.
    Post-condition: Karel is facing a wall and facing North. The column is filled with beepers.
    """
    turn_left()
    if not on_beeper():
        put_beeper()
    while front_is_clear():
        move()
        if not on_beeper():
            put_beeper()


def move_to_next_column():
    """
    Pre-condition: Karel is facing a wall and facing North. The column is filled with beepers.
    Post-condition: Karel is on Street 1 and moved 4 Avenues further, facing East.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        for i in range(4):
            move()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
