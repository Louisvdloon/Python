from neopixel import NeoPixel
from time import sleep
from machine import Pin
np=neopixel.NeoPixel(machine.Pin(23),2)

def lampen(var):
    lijst = [(150,0,0), (100,50,0), (50,100,0), (0,150,0), (0,100,50), (0,50,100), (0,0,150), (50,0,100), (100,0,50)]
    return lijst[var]




