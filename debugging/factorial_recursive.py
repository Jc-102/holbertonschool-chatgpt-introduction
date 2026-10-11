#!/usr/bin/python3
"""
Calculate the factorial of a number given as a command-line argument.
"""
import sys


def factorial(n):
    """
    Function Description:
        Calculates the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The non-negative integer to calculate the factorial of.

    Returns:
        int: The factorial of n (n!). Returns 1 when n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)