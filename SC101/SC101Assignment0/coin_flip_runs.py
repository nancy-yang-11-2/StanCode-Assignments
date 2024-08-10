"""
File: coin_flip_runs.py
Name: Nancy
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
    """
    Create a program to record the results of flipping a coin: H for head and T for tail.
    The user will also decide the number of runs.
    A 'run' is defined as consecutive results. For example 'HHTHHTTT' has 3 runs.
    The program will stop when the coin flipping results reach the number of runs.
    """
    print("Let's flip a coin!")
    a = int(input('Number of runs: '))
    roll1 = r.randrange(1, 3)
    if roll1 == 1:
        roll1 = 'H'
    else:
        roll1 = 'T'
    print(str(roll1), end='')
    run = 0
    can_add_run = True
    while True:
        if run == a:
            break
        else:
            roll2 = r.randrange(1, 3)
            if roll2 == 1:
                roll2 = 'H'
            else:
                roll2 = 'T'
            print(str(roll2), end='')
            if roll1 == roll2:
                if can_add_run == True:
                    run += 1
                    can_add_run = False  # in case getting the same result in the next flip and won't add another run
            else:
                can_add_run = True
                roll1 = roll2


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
    main()
