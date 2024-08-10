"""
File: hailstone.py
Name: Nancy
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program will compute Hailstone sequences, and calculate the steps taken.
    """
    print('This program computes Hailstone sequences', '\n')
    n = int(input('Enter a number: '))  # Ask user to enter a number
    hailstone_sequence(n)


def hailstone_sequence(n):
    step = 0  # Number of steps to reach 1
    while n > 1:
        step += 1
        if n % 2 == 1:
            print(str(n), end='')
            n = 3 * n + 1
            print(' is odd, so I make 3n+1: ', str(n))
        elif n % 2 == 0:
            print(str(n), end='')
            n = n // 2
            print(' is even, so I take half: ', str(n))
    return print('It took', str(step), 'steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
