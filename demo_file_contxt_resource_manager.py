#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close a TEXT file,
# for Reading, Writing and Appending.
"""
    DocString
"""
import sys

movies = { 'hema': ['finding nemo', 'dhurandhar', '83'],
           'kim': ['hot fuzz', 'the princess bride', 'up'],
           'george': ['project hail mary', 'iron man', 'Pirates of the caribbean'],
           'donald': ['lotr', 'the hobbit', 'project hail mary']
}

with open(r"f:\labs\projects\Python_Sep_2026\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name} {movies[name]}", end="\n", file=sys.stdout)
        print(f"{name} {movies[name]}", end="\n", file=fh_out)
        # fh_out.write(f"{name} {movies[name]}\n")
    # End of Block

print("-" * 60 )

with open(r"f:\labs\projects\Python_Sep_2026\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="", file=sys.stdout)
    # End of Block
