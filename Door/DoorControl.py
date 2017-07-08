# Door controls functions
# lock, unlock.py moved to this for compatibility with wrapper



#!/usr/bin/env python
# Unlocks door

import time
import wiringpi
import sys

#sys.path.append('/home/pi/Programming/')
sys.path.append('../lib/')
import Console_lib as console

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

sleep_val = 2
lock_val = 60
unlock_val = 235


def lock_door():
    print('Locking door...')
    wiringpi.pwmWrite(18, lock_val)
    time.sleep(sleep_val)
    console.timeStamp('Door locked.')

def unlock_door():
    print('Unlocking door...')
    wiringpi.pwmWrite(18, unlock_val)
    time.sleep(sleep_val)
    console.timeStamp('Door Unlocked.')

def clean_shutdown():
    # Need this because cant do regular startup/shutdown with modular functions
    # TODO: Fix. this is dumb. Not robust from spamming ctrl+c
    
    print('Shutdown. Releasing servo control...')
    wiringpi.pinMode(18, wiringpi.GPIO.INPUT)
    print('Operation complete.')


