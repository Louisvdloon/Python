from machine import Pin, I2C
import machine
import time
import ssd1306
speaker = machine.Pin(19)
pwm19 = machine.PWM(speaker)
pwm19.freq(800)
pwm19.deinit()
scherm = I2C(-1, scl=Pin(22), sda=Pin(21))
scherm_breedte= 128
scherm_hoogte = 64
oled = ssd1306.SSD1306_I2C(scherm_breedte, scherm_hoogte, scherm)


def shortbeep():
    pwm19.init()
    time.sleep(0.3)
    pwm19.deinit()
    time.sleep(0.5)

def longbeep():
    pwm19.init()
    time.sleep(0.6)
    pwm19.deinit()
    time.sleep(0.5)

def morse(item):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....','I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-','U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..','1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-','?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    # print (MORSE_CODE_DICT[item] )
    for beeps in MORSE_CODE_DICT[item]:
        if beeps == '.':
            shortbeep()
        else:
            longbeep()


woord = 'BAD'
for item in woord:
    morse(item)

for x in range(2):
    oled.text(woord, 0, 30)
    for x in range(scherm_breedte):
        oled.scroll(1, 0)
        oled.show()
        time.sleep_ms(20)

for n in range(2):
    oled.text(woord, 30, 0)
    for n in range(scherm_hoogte):
        oled.scroll(1, 0)
        oled.
        oled.show()
        time.sleep_ms(20)







