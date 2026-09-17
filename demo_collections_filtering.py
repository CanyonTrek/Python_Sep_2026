#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO COPY and OPTIONALLY FILTER
# a source collection to a destination collection using several different ways
""" 
    DocString
"""
students = ['hema', 'hugo', 'joe', 'donald', 'kim', 'tony', 'dingle', 'charlie',
            'maggie', 'hugo']

# ITERATE through the SOURCE collection filtering IN the short name..
# 1. Using a for loop + source, optional condition (filtering), an expression
wee_names = []
for name in students: # 1.Iterator for loop plus source
    if len(name) <= 5: # 2.If condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"1.Short names = {wee_names}")

def filter_names(name):
    """ Return True if name is less than 6 chars """
    if len(name) <= 5:
        return True
    else:
        return False

# 2. Using a for loop + source, USER FUNCTION (filtering), an expression
wee_names = []
for name in students: # 1.Iterator for loop plus source
    if filter_names(name): # 2.If condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"2.Short names = {wee_names}")

# 3. Using built-in filter() function (Iterating), USER FUNCTION (filtering)
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4. Using built-in filter() function (Iterating), LAMBDA FUNCTION (filtering)
wee_names = list(filter(lambda name:len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5. Using LIST COMPREHENSION - expr + for loop + optional condition
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1 Using LIST COMPREHENSION - expr + for loop + optional condition
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2 Using DICT COMPREHENSION - expr + for loop + optional condition
# EXTRA FREE FILTERING - ALL the duplicate KEYS have been removed
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3 Using SET COMPREHENSION - expr + for loop + optional condition
# EXTRA FREE FILTERING - ALL the duplicate VALUES have been removed
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")