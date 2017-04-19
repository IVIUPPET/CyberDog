#!/usr/bin/env python
# Servo control test mode
# Locks, unlocks, and locks the door

import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# Set #18 (pin 6 from the top right) to be a PWM output 
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# Set the PWM mode to milliseconds type
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# Ever important divide down the clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

#delay_period = 0.01

##### End Setup #####

lock_val = 60
unlock_val = 235
sleep_val = 3

print('Defaulting to lock position...')
wiringpi.pwmWrite(18, lock_val)

print('Sleeping...')
time.sleep(sleep_val)

print('Unlocking....')
wiringpi.pwmWrite(18, unlock_val)

print('Sleeping...')
time.sleep(sleep_val)

print('Locking....')
wiringpi.pwmWrite(18, lock_val)

print('Sleeping...')
time.sleep(sleep_val)

print('Releasing Servo Control....')
wiringpi.pinMode(18, wiringpi.GPIO.INPUT)

print('Test mode complete!')
