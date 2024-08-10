"""
File: caesar.py
Name: Nancy
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    A new alphabet order is created by the secret number entered.
    The secret number determines the number of steps that "A" will be moved backward and wrapped around by "Z".
    E.g. if the secret number is 4, "A" will be moved backward by 4 steps.
    Then new alphabet order will become WXYZABCDEFGHIJKLMNOPQRSTUV
    The program will decipher the string entered.
    """
    a = int(input('Secret number: '))
    new_order = ''
    new_order += ALPHABET[len(ALPHABET) - a:]
    new_order += ALPHABET[:len(ALPHABET) - a]
    s = input("What's the ciphered string? ")
    s = s.upper()  # Turn all letters to uppercase to be case-insensitive
    ans = ''
    for i in range(len(s)):
        for j in range(26):
            if s[i].isalpha():
                if s[i] == new_order[j]:  # Check the letter's room number in the new alphabet order
                    ans += ALPHABET[j]    # Replace the letter by the one in the same room number from the old order
                elif s[i] == '':
                    ans += ''
            else:
                ans += s[i]
                break
    print('The deciphered string is: ', ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
