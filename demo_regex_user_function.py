#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a RESUABLE function for
# searching for Regex Patterns in one or more files.
"""
    This scripts contains several functions for searching for
    Regex patterns in one or more files.
"""
import re

# Example of a user function with optional parameter passing
# and default values, and optional return value (lines matched)
def search_pattern(pattern=r"^.{19}$", file=r"f:\labs\words"):
    """ Search for Regex patterns in one or more file and return lines matched """
    fh_in = open(file, mode="rt")
    lines = 0
    reobj = re.compile(pattern) # Compiles pattern ONLY ONCE

    for line in fh_in:
        m = reobj.search(line)  # Match using PRECOMPILED Pattern
        if m:
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
            lines += 1

    fh_in.close() # Close file handle.
    return lines


search_pattern()

num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words")
print(f"Matches {num_lines} lines")
