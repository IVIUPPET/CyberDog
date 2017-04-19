#!/usr/bin/env python
''' A test of wiringpi to detect inputs from PIR sensor and reed switch. '''

import time
import wiringpi
import sys

sys.path.append('/home/pi/Programming/')
import Console_lib as console

# Display version
wiringpi.piBoardRev()

## User params:
pir_pin = 23
reed_pin = 14

run_time = 240 # seconds
#refresh_delay = 0.5
refresh_delay = 1

# Initialize some wiringpi mode
# < pin mode, [GPIO mode], physical pin numbers (P1 only) >
wiringpi.wiringPiSetupGpio()

# Setup ports (0 = input, 1 = output, 2 = alt func, i.e. PWM)
wiringpi.pinMode(pir_pin, 0)
wiringpi.pinMode(reed_pin, 0)

# Activate pullup on door sensor (0 = off, 1 = PD, 2 = PU)
wiringpi.pullUpDnControl(reed_pin, 2)


i = 0
console.timeStamp('Programme running for ' + str(run_time) + ' seconds!')
while i <= run_time:
    if wiringpi.digitalRead(pir_pin):
        console.timeStamp('PIR Triggered', 1)
    if wiringpi.digitalRead(reed_pin):
        console.timeStamp('Reed switch triggered', 1)
    time.sleep(refresh_delay)

    i += 1

console.timeStamp('Programme exiting. Have a nice day.')

# Cleanup. Would normally set as inputs, but just turn off pullup
wiringpi.pullUpDnControl(reed_pin, 0)

''' Additional Support for wiringpi:
http://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
http://raspi.tv/2013/how-to-use-wiringpi2-for-python-with-pull-ups-or-pull-downs-and-pwm
http://raspi.tv/2013/using-the-mcp23017-port-expander-with-wiringpi2-to-give-you-16-new-gpio-ports-part-3
'''
