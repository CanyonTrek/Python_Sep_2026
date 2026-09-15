#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO SPLIT and rjoin strings
# using the str.split() and str.join() methods.
""" 
    DocString
"""
# Sample line from /etc/passwd file on Linux for root user account.
line = "root:x:0:0:The Super User:/root:/bin/bash"

# I want to modify the str! BUT str are immutable!
# Split the str into a list of substrings using the str.split() method.
fields = line.split(":")  # This will return a list of substrings.

# Lists are mutable so can be changed
fields[4] = "The administrator"  # Change the 5th field to a new value.
fields[6] = "/bin/ksh"

line = ":".join(fields) # Returns a new str object
print("Modified line =", line)