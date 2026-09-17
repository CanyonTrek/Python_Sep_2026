#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script defines a class of Tank
""" 
    Tank class for online game
"""
from GOT.app.vehicle import Vehicle

class Tank(Vehicle):
    # Class has TWO components: Attributes (Data) + Behaviour (Methods)
    def __init__(self, country, model):
        Vehicle.__init__(self, country, model)
        self._direction = 0
        self._location = {'x': 0, 'y': 0, 'z': 0}
        self._shells = 20
        self._health = 100
        # No EXPLICIT return as method is IMPLICITLY called.

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # Some SPECIAL Methods
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health

    def __del__(self):
        print(f"Boom..Boom..boom")
        return None

    # Example of a getter and a setter
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # Wrapping the getter/setter with ONE variable name interface
    # tank_health = property(get_health, set_health)
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, new_health):
        self._health = new_health
        return None