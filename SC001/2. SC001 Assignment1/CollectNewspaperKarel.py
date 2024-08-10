"""
File: CollectNewspaperKarel.py
Name: Nancy
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (4, 3), facing East
    Post-condition: Karel picked the newspaper (beeper) at (3, 6) and return to (4, 3).
    """
    move_to_beeper()
    pick_beeper()
    return_home()
    put_beeper()


def move_to_beeper():
    """
    Pre-condition: Karel is at (4, 3), facing East.
    Post-condition: Karel picked the beeper at (3, 6), facing East.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def turn_right():
    # facing East
    for i in range(3):
        turn_left()
    # facing South


def return_home():
    """
    Pre-condition: Karel is at (3, 6), facing East.
    Post-condition: Karel is at (4, 3), facing East.
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()


def turn_around():
    # facing East
    turn_left()
    turn_left()
    # facing West

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
