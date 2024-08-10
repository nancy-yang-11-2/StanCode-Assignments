"""
File: hangman.py
Name: Nancy
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Creating a hangman game. The user has N_TURNS chances to guess the secret word.
    If guess correctly, the letter(s) will be revealed in the correct position(s) of the string.
    Otherwise, one chance will be deducted and the game stops when all chances are consumed.
    """
    r = random_word()
    show = '-' * len(r)
    print("The word looks like", show)
    print('You have 7 wrong guesses left.')
    t = N_TURNS
    while True:
        if show.isalpha():
            print('You win!!')
            print('The answer is: ', r)
            break
        else:
            ch = input('Your guess: ')
            ch = ch.upper()  # turning the letter input to uppercase to be case insensitive
            if ch in r:
                for i in range(len(r)):
                    if ch == r[i]:
                        show = show[:i] + ch + show[i+1:]  # making a new string
                print('You are correct!')
                print('The word looks like:', show)
            else:
                t -= 1
                if t >= 1:
                    print("There's no", ch, "'s in the word.")
                    print('You have', t, 'wrong guess left.')
                else:
                    print("There's no", ch, "'s in the word.")
                    print('You are completely hang :(')
                    print('The answer is', r)
                    return


def random_word() -> object:
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
