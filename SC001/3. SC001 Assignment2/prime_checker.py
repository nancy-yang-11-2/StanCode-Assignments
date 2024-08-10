"""
File: prime_checker.py
Name: Nancy
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -1


def main():
    """
    Make a prime checker to check.
    Check if the input is a prime number.
    """
    print('Welcome to the prime checker!')
    while True:
        n = int(input('n: '))
        if n == EXIT:
            print('Have a good one!')
            break
        if n_is_prime(n):
            print('This is a prime number')
        else:
            print('This is not a prime number')


def n_is_prime(n):
    if n == 2:  # 2 is a prime number
        return True
    if n > 2:
        if n % 2 == 0:  # even numbers as they are not prime
            return False
    i = 3
    while n >= i * i:  # numbers that can be divided by 3, 5, 7 are not prime
        if n % i == 0:
            return False
        i += 2
    return True


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
