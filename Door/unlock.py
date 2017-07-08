#!/usr/bin/env python
# Unlocks door

import time
import wiringpi
import sys

#sys.path.append('/home/pi/Programming/')
sys.path.append('../lib/')
import Console_lib as console

def unlock_door():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

    sleep_val = 2
    lock_val = 60
    unlock_val = 235

    print('Unlocking door...')
    wiringpi.pwmWrite(18, unlock_val)
    time.sleep(sleep_val)

    print('Releasing servo control...')
    wiringpi.pinMode(18, wiringpi.GPIO.INPUT)
    print('Operation complete.')

    console.timeStamp('Door Unlocked.')
