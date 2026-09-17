#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is an ULTRA realistic Calculator App with Basic and Advanced functions
""" 
    Calculator App with Basic and Advanced functions
"""

menu = """
        Menu Options
        ------------
        1.Display Basic Calc examples
        2.Display Advanced Calc examples
        q=Quit
"""
import sys
from app import basic # SAFER
from app.adv import power, mod, sqrt

def main():
    while True:
        print(menu)
        option = input("Enter option (1-2,q=quit): ")
        match option:
            case "1":
                print(f"20 + 19 + 18 = {basic.add(20, 19, 18)}")
                print(f"20 * 19 * 18 = {basic.mul(20, 19, 18)}")
                print(f"20 / 18 = {basic.div(20, 18)}")
            case "2":
                print(f"20 ** 2 = {power(20, 2)}")
                print(f"20 * 19 * 18 = {mod(20, 19)}")
                print(f"\N{square root}20 = {sqrt(20)}")
            case "q":
                print("Quitting..")
                break
            case _:
                print("Invalid option")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as module
    main()
    sys.exit(0) # Exit with return code (0=success)






