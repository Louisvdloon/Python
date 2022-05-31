from neopixel import NeoPixel
from time import sleep
from machine import Pin
np=neopixel.NeoPixel(machine.Pin(23),2)

def lampen(var):
    lijst = [(255, 0, 0), (0, 255, 0), (182, 72, 0)]
    return lijst[var]

#variable voor de knoppen en leds
np = NeoPixel(Pin(23), 2)
#knop 1 en 2 op pin 16 en 17
k1 = Pin(16, Pin.IN)
k2 = Pin(17, Pin.IN)

#functie voor het stoplicht te triggeren dat er iemand op het fietspad/voetpad staat te wachten
def trafficlightv2():



     #zet de lampen weer uit
    np[0] = (0,0,0)
    np.write()

