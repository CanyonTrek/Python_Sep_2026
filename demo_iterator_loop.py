#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO ITERATE through a SEQUENCE
# using an ITERATOR for loop.
""" 
    DocString
"""
import sys
#              0                1                2
heroes = ['ryan giggs', 'david attenborough', 'big sam',
          'thierry henry', 'nicole']

# ITERATE through the heroes list using an ITERATOR for loop.
for hero in heroes:
    print(hero, end="\n")  # end="\n" is the default, so this is optional

# ITERATE through the list and modify the objects using an ITERATOR for loop.
idx = 0
for hero in heroes:
    print(hero.upper())
    heroes[idx] = hero.upper()
    idx += 1
print("Heroes =", heroes)

# ITERATE through the list and modify the objects using an ITERATOR for loop
# and the built-in enumerate() function.
for (idx, hero) in enumerate(heroes, start=0):
    print(hero.title())
    heroes[idx] = hero.title()
print("Heroes =", heroes)

try:
    sys.exit(66) # Exit the script with a success status code (0), errors=1-255
    # sys.exit("Goodbye") # Return EXPR to STDERR (displayed in RED) and error code 1 (default)
except SystemExit:
    print("Exiting the script...")
    raise  # Re-raise the SystemExit exception to exit the script
