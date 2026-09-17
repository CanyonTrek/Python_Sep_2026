#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module is a collection of advanced functions
# for a calculator app
""" 
    Advanced functions for Calculator App including
    power, modulus and square root functions
"""
import sys

def power(x, z):
    """ Return the power of x to the power z """
    return float(x**z)

def mod(x, z):
    """ Return the remainder of x divided by z """
    return float(x % z)

def sqrt(x):
    """ Return the Square root of x as a float """
    return float(x**0.5)

def main():
    print("--------- Advanced Examples---------")
    print(f"9 ** 8 = {power(9, 8)}")
    print(f"9 % 8 = {mod(9, 8)}")
    print(f"\N{square root}8 = {sqrt(8)}")
    print("------------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as module
    main()
    sys.exit(0) # Exit with return code (0=success)