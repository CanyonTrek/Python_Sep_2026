#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO display the entire
# unicode charset in a terminal window.
""" 
    DocString
"""
# ITERATE through all the unicode char positions.
for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print("\n")
    except UnicodeEncodeError:
        print(" ")