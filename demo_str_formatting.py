#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO format strings using
# different techniques including str concatenation, escape chars
# and using str methods and f-strings!
"""
    DocString
"""
# Dictionary of planet info and distance to sun in GM.
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# Iterate through keys in the planets dict and display planet info
# using an ITERATOR for loop and str concatenation and escape chars. MEH!
for planet in planets.keys():
    print("\t\t" + planet + ": \t" + str(planets[planet]) + " Gm")

print("-" * 50)
# using an ITERATOR for loop and str concatenation and str justification. OK!
for planet in planets.keys():
    print(planet.rjust(12) + ":" + str(planets[planet]).rjust(12, '.') + " Gm")

print("-" * 50)
# using an ITERATOR for loop and str.format() method. GOOD! Py3 onwards
for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm".format(planet, planets[planet]))

print("-" * 50)
# using an ITERATOR and f-strings. BEST! Py3.5 onwards
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm")