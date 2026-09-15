#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will simulate a high street bank PIN ATM.
# Maximum or 3 attempts to enter the correct PIN.
""" 
    DocString
"""

master_pin = "1234"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Please enter your PIN: ")
    if pin == master_pin:
        print("Access granted.")
        break
    else:
        print("Incorrect PIN. Please try again.")
        attempts += 1
else:
    # Executes ONLY ONCE when while loop becomes False, i.e. when attempts >= 3
    print("Too many attempts: Access denied")
    print("Your card has been retained. Hava a nice day")


print("Done.")