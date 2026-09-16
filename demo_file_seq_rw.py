#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close a TEXT file,
# for Reading, Writing and Appending.
""" 
    DocString
"""
movies = { 'hema': ['finding nemo', 'dhurandhar', '83'],
           'kim': ['hot fuzz', 'the princess bride', 'up'],
           'george': ['project hail mary', 'iron man', 'Pirates of the caribbean'],
           'donald': ['lotr', 'the hobbit', 'project hail mary']
}
# Open file handle for WRITING in TEXT mode
fh_out = open(r"f:\labs\projects\Python_Sep_2026\movies.txt", mode="wt")

# ITERATE through dict keys and write movie info to file.
for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n")
    fh_out.write(f"{name} {movies[name]}\n")

# fh_out.flush() # Flush buffers
fh_out.close() # Flush buffers and close file handle

print("-" * 60 )

# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\projects\Python_Sep_2026\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str! Be Careful!
# text = fh_in.read(30) # Read NEXT 30 chars into str!
# text = fh_in.readline() # Read NEXT LINE into str!
# lines = fh_in.readlines() # Read ENTIRE file into LIST! BE Careful!
# print(f"First line is {lines[0]}")
# print(f"Last line is {lines[-1]}")

# ITERATE through the file handle one line at a time..
# Using an ITERATOR for loop plus filehandle (ITERATOR Obj = next/iter)
for line in fh_in:
    print(line, end="")

fh_in.close()