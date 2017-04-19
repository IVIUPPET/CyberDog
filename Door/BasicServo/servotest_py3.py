#!/usr/bin/env python3
# Servo Control
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

# Mod so it doesn't go forever
i = 0
#while True:
while i < 1:
    for pulse in range(50, 250, 1):
        print('Writing pulse to pin 18')
        wiringpi.pwmWrite(18, pulse)
        print('Sleeping...')
        time.sleep(delay_period)
    for pulse in range(250, 50, -1):
        print('Writing alt pulse to pin 18')
        wiringpi.pwmWrite(18, pulse)
        print ('sleeping')
        time.sleep(delay_period)
    i = i+1

time.sleep(1)

# Test left/right position
run_cycles = 100
print('Move left')
pulse = 50
i = 0
while i < run_cycles:
#    wiringpi.pwmWrite(18, pulse)
    time.sleep(delay_period)
    i = i+1

time.sleep(1)

print('Move right')
pulse = 250
i = 0
while i < run_cycles:
    wiringpi.pwmWrite(18, pulse)
    time.sleep(delay_period)
    i = i+1


### Clean up
wiringpi.digitalWrite(18, 0) # Sets port 18 to 0 (0 V, off)
wiringpi.pinMode(18, 0) # Sets GPIO 18 to input mode 
