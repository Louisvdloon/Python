# Write your code here :-)
import machine
import time
speaker = machine.Pin(19)
pwm19 = machine.PWM(speaker)
pwm19.freq(800)
pwm19.deinit()


letterlist = ("N", "A", "S")

def lang():
    pwm19.init()
    time.sleep(0.5)
    pwm19.deinit()
    time.sleep(0.5)

def kort():
    pwm19.init()
    time.sleep(0.3)
    pwm19.deinit()
    time.sleep(0.5)

def morse_n():
    lang()
    kort()

def morse_a():
    kort()
    lang()

def morse_s():
    kort()
    kort()
    kort()


def lettercheck():
    while test() not in letterlist:
        test()



