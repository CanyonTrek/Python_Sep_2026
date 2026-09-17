#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a user function using the
# def statement and the lambda functions (anonymous functions)
""" 
    DocString
"""

def add(*args):
    """ Return the SUM of all arguments """
    return sum(args)

print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")

# Alternatively we could use a lambda function (anonymous function)
# if the function is SIMPLE and not used anywhere else..
print(f"4 + 3 + 2 + 1 = {(lambda *args:sum(args))(4, 3, 2, 1)}")