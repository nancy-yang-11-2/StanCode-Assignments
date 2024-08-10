"""
File: quadratic_solver.py
Name: Nancy
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    The program will solve the quadratic equation and show the results.
    When discriminant > 0, there are 2 roots.
    When discriminant = 0, there is 1 root.
    When discriminant < 0, there are no real roots.
    """
    print('stanCode Quadratic Solver!')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))

    # define the discriminant
    q = (b * b) - (4 * a * c)

    # when q > 0, there are 2 roots; q == 0, there is 1 root; q < 0 the equation will fail therefore no real roots
    if q > 0:
        x1 = (-b + math.sqrt(q)) / (2 * a)
        x2 = (-b - math.sqrt(q)) / (2 * a)
        print('Two roots: ', str(x1), ', ', str(x2))
    elif q == 0:
        x1 = (-b + math.sqrt(q)) / (2 * a)
        print('One root: ', str(x1))
    elif q < 0:
        print('No real roots')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
