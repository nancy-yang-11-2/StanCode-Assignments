"""
File: CheckerboardKarel.py
Name: Nancy
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (1, 1) facing East.
    Post-condition: Karel filled the world with beepers and with a space in between each beepers.
    """

    while front_is_clear():
        put_beeper()
        fill_the_row()
        move_to_next_row()
    put_beeper()
    turn_left()
    fill_the_column()


def fill_the_row():
    """
    Pre-condition: Karel is on the right of a wall, facing East.
    Post-condition: Karel is on the left of a wall , facing East. The row is filled with beepers on every other column.
    """
    while front_is_clear():
        if on_beeper():
            move()
        if front_is_clear():
            move()
            if not on_beeper():
                put_beeper()


def move_to_next_row():
    """
    Pre-condition: Karel is on the left of a wall , facing East. The row is filled with beepers on every other column.
    Post-condition: Karel is on the right of a wall, a Street above, facing East.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        if on_beeper():
            move()
            turn_right()
            move()
        else:
            move()
            turn_right()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def fill_the_column():
    """
    Pre-condition: Karel is in front of a wall, facing North.
    Post-condition: Karel is facing wall, facing North. The column is filled with beepers on every other row.
    """
    while front_is_clear():
        if on_beeper():
            move()
        if front_is_clear():
            move()
            if not on_beeper():
                put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
