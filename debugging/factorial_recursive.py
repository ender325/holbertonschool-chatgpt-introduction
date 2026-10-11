#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function description:
        Calculates the factorial of a number recursively.

    Parameters:
        n (int): The non-negative integer to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
