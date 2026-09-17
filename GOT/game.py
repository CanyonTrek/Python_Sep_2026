#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is a Game of Tanks
""" 
    GOT - Game of Tanks
"""
import sys
from app import tank

def main():
    # Create/Instantiate 3 Tank objects
    kim_tank = tank.Tank("german", "tiger")
    joe_tank = tank.Tank("american", "sherman")
    tony_tank = tank.Tank("british", "churchill")

    # and the game begins..
    kim_tank.accel(61)
    joe_tank.accel(34)

    tony_tank.rotate_left(289)
    tony_tank.accel(23)
    tony_tank.shoot()

    # ..and success
    kim_tank.take_damage(61)
    joe_tank.take_damage(22)

    # ..and now for some game visuals.
    print(f"Health of Kim's tank is {kim_tank._health}") # POOR CODE

    print(f"Health of Kim's and Joe's Tank = {kim_tank + joe_tank}")

    # Kim has received a Health boost
    # kim_tank._health = 100
    # print(f"New health of Kim's tank is {kim_tank._health}")
    kim_tank.set_health(101) # SETTER method :-)
    print(f"New health of Kim's tank is {kim_tank.get_health()}") # GETTER method :-)

    kim_tank.tank_health = 102 # Property Variable :-)
    print(f"New health of Kim's tank is {kim_tank.tank_health}")
    return None

# Namespace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)

