"""
File: rocket.py
Name: Nancy
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 6


def main():
    """
    Create a program to draw a rocket.
    The rocket is composed of 6 parts, each part is drew by a for loop function.
    """
    print_head()
    print_belt()
    print_upper()
    print_lower()
    print_belt()
    print_head()


def print_head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ", end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print("")


def print_belt():
    print('+', end='')
    for i in range(SIZE*2):
        for j in range(1):
            print('=', end='')
    print('+')


def print_upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(i+1):
            print('/', end='')
            print('\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        print('|', end='')
        print('')


def print_lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\', end='')
            print('/', end='')
        for j in range(i):
            print('.', end='')
        print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
