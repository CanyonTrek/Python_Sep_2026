#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module is a collection of basic
# calculator functions
""" 
    Basic functions for a Calculator App including
    add, multiply and divide
"""
import sys

def add(*args):
    """ Return SUM of all parameters
    >>> add(4, 3, 2, 1)
    10.0
    >>> add(10, 20)
    30.0
    """
    total = 0
    for num in args:
        total += num
    return float(total)

def mul(*args):
    """ Return PRODUCT of all parameters
    >>> mul(4, 3, 2)
    24.0
    """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return the quotient of x divided by z
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

def main():
    print("--------- Basic Examples---------")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    print("---------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as module
    import doctest
    doctest.testmod()
    main()
    sys.exit(0) # Exit with return code (0=success)
