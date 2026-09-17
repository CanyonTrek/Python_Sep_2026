#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a VARIADIC function that
# allows a VARIABLE number of parameters.
"""
    DocString
"""
import re

# Example of a VARIADIC function that accepts a variable
# number of parameters.
def search_pattern(pattern=r"^.{19}$", *files):
    lines = 0
    for file in files:
        fh_in = open(file, mode="rt")
        reobj = re.compile(pattern) # Compiles pattern ONLY ONCE

        for line in fh_in:
            m = reobj.search(line)  # Match using PRECOMPILED Pattern
            if m:
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
                lines += 1

        fh_in.close() # Close file handle.
    return lines


num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words", r"f:\labs\words2")
print(f"Matches {num_lines} lines")
