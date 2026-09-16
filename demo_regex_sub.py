#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match and SUBSTITUTE patterns
# of text using Regex pattern matching and the re.sub() and subn() methods
""" 
    DocString
"""
import re
# Sample line from /etc/passwd on Linux for the root user account
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# I want to modify the string, BUT str are immutable!
line = re.sub(r"[sS]uper [uU]ser", r"Administrator", line) # Returns a modified str
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns a TUPLE (modified str, num changes)

print(f"Modified line = {line} with {num} change")