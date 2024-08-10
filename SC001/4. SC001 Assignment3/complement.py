"""
File: complement.py
Name: Nancy
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Change A to T and vice versa.
    Change C to G and vice versa.
    """
    build_complement()


def build_complement():
    s = input('Please enter DNA stand: ')
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        elif ch == 'G':
            ans += 'C'
        else:
            print('DNA strand is missing.')
    print(ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
