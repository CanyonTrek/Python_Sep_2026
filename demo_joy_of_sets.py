#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, and grown and shrink,
# and COMBINE sets in Python.
# set is (UNORDERED Collection of UNIQUE items) in Python
""" 
    DocString
"""
marvel_fans = {'george', 'kim', 'joe', 'donald', 'grace', 'isla'}
dc_fans = set() # Create and empty set

# Grow a set..
dc_fans.add('donald') # Add a single item to the set
dc_fans.add('hema') # Add a single item to the set
dc_fans.add('hugo') # Add a single item to the set

# Access a set..
print(f"Marvel fans are: {marvel_fans}")
print(f"DC fans are: {dc_fans}")

# Shrink a set..
# dc_fans.remove('hema') # Remove a single item from the set
# dc_fans.discard('hugo') # Remove a single item from the set (No error if not found).
# dc_fans.pop() # Remove a random item from the set
# print(f"DC fans are: {dc_fans}")
print("-" * 50)
# COMBINE sets..REMEMBER VENN DIAGRAMS
print(f"Fans of Marvel or DC fans: {marvel_fans.union(dc_fans)}")
print(f"Fans of both Marvel AND DC fans: {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel: {marvel_fans.difference(dc_fans)}")
print(f"Fans of EITHER Marvel OR DC: {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 80)
# COMBINE sets using operators..REMEMBER VENN DIAGRAMS
print(f"Fans of Marvel or DC fans: {marvel_fans | dc_fans}")
print(f"Fans of both Marvel AND DC fans: {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel: {marvel_fans - dc_fans}")
print(f"Fans of EITHER Marvel OR DC: {marvel_fans ^ dc_fans}")