#!/bin/python
# Single button handler with short and long press for reboot and shutdown
# Uses interrupt driven blocking wait falling edge detection without debounce

import RPi.GPIO as GPIO
import time
import os

PIN = 3 # GPIO Button Input - use on GPIO3 (Pin 5) for restart from halt

# Use Broadcom SOC pin numbering with internal pullup enabled
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while 1:
    if GPIO.wait_for_edge(PIN, GPIO.FALLING):
        print "Button Pressed"
        time.sleep(2)
        if GPIO.input(PIN) == 0:
            # long press
	    print "Long Press"
            os.system("sudo poweroff")
        else:
	    # short press
            print "Short Press"
            os.system("sudo reboot")
