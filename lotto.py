#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO generate 6 UNIQUE
# random lottery numbers
"""
    DocString
"""
import random

# lotto = [] # Create an empty list

# while len(lotto) < 6:
#    num = random.randint(1, 50)
#    if num not in lotto:
#        lotto.append(num) # Add the number to the list
#    else:
#        print("Duplicate number =", num)

lotto = set() # Create an empty set

while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num) # Add the number to the set (duplicates are ignored)


print("Lottery numbers:", sorted(lotto)) # Print the list of numbers