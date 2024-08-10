"""
File: class_reviews.py
Name: Nancy
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = str(-1)    # -1 is int, it cannot be compared with data entered to 'Which class?', therefore convert to str


def main():
    """
    Create a program to get test scores for class SC001 and SC101.
    Identify the maximum, minimum, and average score of both classes.
    """

    s = str(input('Which class? '))
    s = s.upper()    # convert to uppercase to be case insensitive
    if s == EXIT:
        print('No class scores were entered')
    else:
        a = int(input('Score: '))
        max001 = 0
        min001 = 10
        count001 = 0
        total001 = 0
        max101 = 0
        min101 = 10
        count101 = 0
        total101 = 0
        if s == 'SC001':
            count001 += 1
            total001 += a
            max001 = a
            min001 = a
        else:
            count101 += 1
            total101 += a
            max101 = a
            min101 = a
        while True:
            s = str(input('Which class? '))
            s = s.upper()    # convert to uppercase to be case insensitive
            if s == EXIT:
                break
            else:
                a = int(input('Score: '))
                if s == 'SC001':
                    if a > max001:
                        max001 = a
                    if a < min001:
                        min001 = a
                    count001 += 1
                    total001 += a
                else:
                    if a > max101:
                        max101 = a
                    if a < min101:
                        min101 = a
                    count101 += 1
                    total101 += a
        for i in range(13):
            print('=', end='')
        print('SC001', end='')
        for i in range(13):
            print('=', end='')
        print('')
        if count001 == 0:    # when there's no data enter to class SC001
            print('No score for SC001')
        else:
            print('Max (001): ', int(max001))
            print('Min (001): ', int(min001))
            avg001 = total001 / count001
            print('Avg (001): ', float(avg001))
        for i in range(13):
            print('=', end='')
        print('SC101', end='')
        for i in range(13):
            print('=', end='')
        print('')
        if count101 == 0:    # when there's no data enter to class SC101
            print('No score for SC101')
        else:
            print('Max (101): ', int(max101))
            print('Min (101): ', int(min101))
            avg101 = total101 / count101
            print('Avg (101): ', float(avg101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
