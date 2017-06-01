#!/usr/bin/env python
''' Basic door entrance detection '''
''' Changelog:
    V1.1(c): Added logging,
    V1.0: Proof of concept
    '''

import time
import wiringpi
import sys

#sys.path.append('/home/pi/Programming/')
sys.path.append('../lib/')
import Console_lib as console

##############################################################################
# User params:
log_fname = 'log.txt'
##############################################################################

# Display version
wiringpi.piBoardRev()

## User params:
pir_pin = 23
reed_pin = 14

run_time = 240 # seconds
#refresh_delay = 0.5
refresh_delay = 1

event_refresh_rate = 0.2 # care more about accuracy when event detected

# Initialize some wiringpi mode
# < pin mode, [GPIO mode], physical pin numbers (P1 only) >
wiringpi.wiringPiSetupGpio()

# Setup ports (0 = input, 1 = output, 2 = alt func, i.e. PWM)
wiringpi.pinMode(pir_pin, 0)
wiringpi.pinMode(reed_pin, 0)

# Activate pullup on door sensor (0 = off, 1 = PD, 2 = PU)
wiringpi.pullUpDnControl(reed_pin, 2)
 
# TODO: add sim mode so don't have to open door sensor each time to test lol

i = 0
console.timeStamp('Programme running!')
while True: 
    if wiringpi.digitalRead(reed_pin): 
        # The reed switch has been triggered
        #print('Door opened!')
        #console.timeStamp('Door opened!', 1)
        console.log(console.timeStamp('Door opened!', 1), log_fname)
        j = 0
        while wiringpi.digitalRead(reed_pin):
            time.sleep(event_refresh_rate)
            j += 1
        console.log(console.timeStamp('Door closed.'), log_fname)
        big_string = 'Door was open for ' + '{:0.2f}'.format(j*event_refresh_rate) + ' seconds.' # Python doesn't like this heap put into a function
        # Must cat into a str before passing
        # TODO: format hh:mm:ss for when a fight breaks out and the sensor falls off for 1080 seconds until the cops come. messy, hard to use that number
        #console.timeStamp(big_string)
        print(big_string)
        console.log(big_string, log_fname)
        #print('Door closed.')
        

    time.sleep(refresh_delay)

console.timeStamp('Programme exiting. Have a nice day.')

# Cleanup. Would normally set as inputs, but is, just turn off pullup
wiringpi.pullUpDnControl(reed_pin, 0)

''' Additional Support for wiringpi:
http://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
http://raspi.tv/2013/how-to-use-wiringpi2-for-python-with-pull-ups-or-pull-downs-and-pwm
http://raspi.tv/2013/using-the-mcp23017-port-expander-with-wiringpi2-to-give-you-16-new-gpio-ports-part-3
'''
