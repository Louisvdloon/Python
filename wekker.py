# Alle libraries die ik gebruik en alle variables die ik aangemaakt heb
from machine import Pin, I2C
import machine
import ssd1306
from time import sleep
import framebuf
import ntptime
import time
k1 = Pin(16, Pin.IN)
k2 = Pin(17, Pin.IN)
scherm = I2C(-1, scl=Pin(22), sda=Pin(21))
scherm_breedte = 128
scherm_hoogte = 64
oled = ssd1306.SSD1306_I2C(scherm_breedte, scherm_hoogte, scherm)
ntptime.host = "3.nl.pool.ntp.org"

speaker = machine.Pin(19)
pwm19 = machine.PWM(speaker)
pwm19.freq(800)
pwm19.deinit()
t = time.localtime()

def wekkersound():
    #flag1 is een flag die de while loop beheerst
    #Zodra flag1 + 1 gaat breekt hij uit de loop
    #De eerste loop is het geluid van de wekker
    #De tweede loop is om de wekker uit te zetten
    #De derde loop is om je wekker op snooze te zetten (Wekker gaat 5 seconden later weer af)
    flag1 = 0
    while flag1 == 0:
        pwm19.init()
        time.sleep(1)
        pwm19.deinit()
        time.sleep(1)

        while k1.value() == 1:
            pwm19.deinit()
            flag1 = flag1 + 1
        while k2.value() == 1:
            pwm19.deinit()
            sleep(5)
            pwm19.init()
            time.sleep(1)
            pwm19.deinit()
            time.sleep(1)

#De variables die ik gebruik om de wekker makkelijk mee in te stellen
hour = 22
minute = 30


#Laat de tijd op het scherm zien en kijkt of de tijd overeen komt met de opgegeven tijd in de variables.
#komt het overeen? dan voert hij de functie 'wekkersound()' uit
def wekker():
    hour = 14
    minute = 10
    flag2 = 0
    while flag2 == 0 or 1:
        t = time.localtime()
        oled.fill(0)    #{} perse nodig! anders doet .format niks
        oled.text('Tijd: {}' .format(t[3] + 2), 0, 1)
        oled.text('      {}' .format(":"), 14, 1)
        oled.text('      {}' .format(t[4]), 20, 1)
        oled.show()         #De coordinaten
        # als hour op 999 staat en minute op 999 dan staat de wekker uit
        if hour == 999 and minute == 999:
            oled.text('Alarm: Uit', 0, 26)
            oled.show()
        else:
            oled.text('Alarm: {}'.format(hour), 0 ,26)
            oled.text('      {}' .format(":"), 26, 26)
            oled.text('      {}' .format(minute), 36, 26)
            oled.show()

        if flag2 == 0 and t[3] == hour and t[4] == minute:
            wekkersound()
            flag2 = flag2 + 1



