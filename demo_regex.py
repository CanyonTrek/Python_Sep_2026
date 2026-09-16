#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text using str testing and
# pattern matching using Regex and re.py module.
""" 
    DocString
"""
import re
# Open file handle for READING in TEXT mode.
fh_in = open(r"f:\labs\words", mode="rt")

# Iterate through the file handle reading one line at a time
# using an ITERATOR for loop.
for line in fh_in:
    # Example of str testing
    # if (line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line):
    # Example of Regex testing
    # m = re.search(r"^the", line) # Match lines STARTING with 'the'
    # m = re.search(r"ing$", line) # Match lines ENDING with 'ing'
    # m = re.search(r"^.ing$", line)  # Match lines of 4 chars ending in 'ing'
    # m = re.search(r"^[adpr]ing$", line)  # Match lines of 4 chars ending in 'ing'
    # m = re.search(r"^[A-Z]", line)  # Match lines STARTING with a CAPITAL
    # m = re.search(r"^...................$", line)  # Match lines exactly 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines exactly 19 chars
    # m = re.search(r"^...................", line)  # Match lines at least 19 chars
    # m = re.search(r"\.", line)  # Match lines with a DOT
    # m = re.search(r"[.]", line)  # Match lines with a DOT
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines with 3 VOWELS
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines at least 5 consecutive VOWELS
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines START/END with a CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match lines START/END with a CAPITAL
    # m = re.search(r"^(.)(.).\2\1$", line)  # Match lines 5 char palindromes
    m = re.search(r"^([A-Z]).*\1$", line, flags=re.I)  # Match lines START/END with SAME CAPITAL
    # m = re.match(r"(.)(.).\2\1$", line)  # match() AUTO matches START of LINE
    # m = re.fullmatch(r"^(.)(.).\2\1\n$", line)  # Match ENTIRE line including HIDDEN chars

    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}, "
              f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")

fh_in.close() # Close file handle.
