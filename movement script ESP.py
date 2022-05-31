# Dit zijn alle libraries en variables die ik gebruik.
from machine import Pin, I2C
import machine
import ssd1306
# Alle libraries die ik gebruik en alle variables die ik aangemaakt heb
import neopixel
from time import sleep
import framebuf
k1 = Pin(16, Pin.IN)
k2 = Pin(17, Pin.IN)
scherm = I2C(-1, scl=Pin(22), sda=Pin(21))
scherm_breedte = 128
scherm_hoogte = 64
oled = ssd1306.SSD1306_I2C(scherm_breedte, scherm_hoogte, scherm)

# Dit laat de pixel zien midden in het scherm
# 64 staat voor x en de 32 voor y. de 1 staat voor aan of uit
# oled.show() moet je altijd gebruiken om de pixel in beeld te laten komen
oled.pixel(64, 32, 1)
oled.show()

# Dit is een functie die het movement script uitvoert!
# WARNING! voer deze functie alleen uit in de terminal. Anders mag je je ESP device flashen door de while loop die erin verwerkt zit
def movement():
    middenx = 64
    while True:
        if k1.value() == 1:
            middenx = middenx - 3
        if k2.value() == 1:
            middenx = middenx + 3

        oled.fill(0)
        oled.pixel(middenx, 32, 1)
        oled.show()








