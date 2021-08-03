from mpython import *

from bluebit import *

import time

hcsr04 = HCSR04(trigger_pin=Pin.P16, echo_pin=Pin.P15)
ultrasonic = Ultrasonic()
oled.fill(0)
oled.DispChar('Hello, world!', 10, 0, 1)
oled.show()
while True:
    oled.fill_rect(0, 16, 128, 16, 0)
    oled.DispChar(('²âÁ¿½á¹û' + str(ultrasonic.distance())), 0, 16, 1)
    oled.show()
    time.sleep(5)
