"""
File: string_score.py
Name: Nancy
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    Create a score function.
    This function will assign a score to each letter/digit of the string entered and calculate the sum.
    A digit gets 1 score, an uppercase letter gets 2 scores, a lowercase letter gets 3 scores.
    """
    score('1aB4rC')   # 12
    score('aaaaA3')   # 15


def score(string):
    ans = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            ans += 1
        elif ch.isupper():
            ans += 2
        elif ch.islower():
            ans += 3
    print(str(ans))


if __name__ == '__main__':
    main()