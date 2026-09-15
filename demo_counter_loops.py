#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo different ways top write a COUNTER loop
""" 
    DocString
"""

count = 0 # 1. Initialise the counter variable
while count < 10: # 2. Condition to check if the counter is less than 10
    print(count)
    count += 1 # 3. Increment the counter variable by 1

# Alternative way to write a counter loop using a for loop
# and the built-in range(start, stop, step) function.
for num in range(0, 10, 1):
    print(num)

# and the built-in range(start, stop, step=1) function.
for num in range(0, 10):
    print(num)

# and the built-in range(start=0, stop, step=1) function.
for num in range(10):
    print(num)