# Likelyhood of a false positive is much less if you use two sensors!

# This is a test of this hypothesis

import time
import RPi.GPIO as io
io.setmode(io.BCM)

pir1_pin = 14
pir2_pin = 15 # declare signal pins as per 'GPIO designation'

# Activate two inputs, no Pup necessary
io.setup(pir1_pin, io.IN) 
io.setup(pir2_pin, io.IN)

while True:
    if io.input(pir1_pin):
        print('PIR Alarm 1!')
    if io.input(pir2_pin):
        print('PIR Alarm 2!')
    time.sleep(0.5)
