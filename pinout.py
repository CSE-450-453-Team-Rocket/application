# --------------- #
# Team Rocket 2023
# Author unknown, Marcos De La Osa Cruz
# class contains the pinouts for the raspberry pi pins

from enum import Enum

class Pinout(Enum):
    testing = 1     # Pin left alone for testing purposes

#!!!!!! Not sure of the exact pinout for the switches yet !!!!!!#
    activateL = 1   # Left activation switch (green LED enabled switch for left launch drum)   
    activateR = 2   # Right activation switch (green LED enabled switch for right launch drum)   
    button = 3      # Button on controller
    joystickL = 4   # Left joystick on controller
    joystickR = 5   # Right joystick on controller
