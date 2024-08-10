"""
File: MidpointKarel.py
Name: Nancy
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (1, 1), facing East.
    Post-condition: Karel is standing on the midpoint, on a beeper, facing East.
    """
    fill_both_ends()
    return_home()
    move_beepers_to_center()
    go_to_midpoint()


def fill_both_ends():
    """
    Pre-condition: Karel is at (1, 1), facing East.
    Post-condition: There's a beeper at (1, 1).
    Karel is standing on a beeper on Street 1, facing a wall and facing East.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()


def return_home():
    """
    Pre-condition: Karel is facing a wall, facing East.
    Post-condition: Karel is at (1, 1), facing East.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


def move_beepers_to_center():
    """
    Pre-condition: There are 2 beepers on both ends of Street 1.
    Post-condition: There are 2 beepers at the midpoint of Street 1.
    """
    pick_beeper()
    move()
    put_beeper()
    move()
    while front_is_clear():
        if not on_beeper():
            move()
        if on_beeper():
            turn_around()
            pick_beeper()
            move()
            put_beeper()
            move()
    if not front_is_clear():
        turn_around()
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()


def go_to_midpoint():
    """
    Pre-condition: Karel is facing a wall.
    Post-condition: Karel is standing on the midpoint, on a beeper, facing East.
    """
    turn_around()
    while not on_beeper():
        if front_is_clear():
            move()
    if not facing_east():
        turn_around()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
