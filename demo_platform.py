#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO find out
# which platform your script is running on!
""" 
    DocString
"""
import sys
import platform
import os

if sys.platform == "win32":
    print("You are running on Windows")
    h_dir = os.environ['HOMEPATH']
    h_dir = os.path.join(h_dir, 'photos')
elif sys.platform == "linux" or sys.platform == "Darwin":
    print("You are running on Linux")
    h_dir = os.environ['HOME']
    h_dir = os.path.join(h_dir, 'photos')

print("Photos folder is: " + h_dir)


if platform.system() == "Windows":
    print("You are running on Windows")
elif platform.system() == "Darwin":
    print("You are running on MacOS")
elif platform.system() == "Linux":
    print("You are running on Linux")