#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, name and call a
# user function with optional parameters and return value.
""" 
    DocString
"""
# Example of a user function
# with optional parameter passing
# with optional named parameters *,
# with optional default values
def say_hello(greeting="bonjour", recipient="mes ami"):
    message = greeting + " " + recipient
    print(message)
    return None

say_hello("hello", "my friends") # Positional parameter passing
say_hello(greeting="hola", recipient="mi amigos") # Named parameter passing
say_hello(recipient="meus amigos", greeting="ola") # Named parameters in different order
say_hello("vanakkam", recipient="nanbarkale") # Mixed (positional->named)
say_hello("bonjour")
say_hello()



