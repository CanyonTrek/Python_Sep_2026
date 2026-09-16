#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO Open and close file
# for RANDOM access using the .seek() and .tell() methods
"""
    DocString
"""
import sys
SOF = 0 # Start of file
CUR = 1 # Current file position
EOF = 2 # End of File

with open(r"f:\labs\projects\Python_Sep_2026\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, SOF) # Seek forwards 135 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

with open(r"f:\labs\projects\Python_Sep_2026\movies.txt", mode="rb") as fh_in:
    fh_in.seek(-90, EOF) # Seek back 90 bytes from EOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-70, CUR) # Seek back 70 bytes from current position
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")