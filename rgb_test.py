#!/usr/bin/python
import time
import RPi.GPIO as GPIO
 
# Define enable and disable states
RGB_ENABLE = 1
RGB_DISABLE = 0
 
#LED CONFIG - Set GPIO Ports
RGB_RED = 16
RGB_GREEN = 18
RGB_BLUE = 22
RGB = [ RGB_RED, RGB_GREEN, RGB_BLUE]
 
def led_setup():
    #Set up the wiring
    GPIO.setmode(GPIO.BOARD)
    # Setup Ports
    for val in RGB:
        GPIO.setup(val, GPIO.OUT)
 
def led_activate( color ):
    GPIO.output( color, RGB_ENABLE )
 
def led_deactivate( color ):
    GPIO.output( color, RGB_DISABLE )
 
def led_clear():
    for val in RGB:
        GPIO.output(val, RGB_DISABLE)
 
def main():
    led_setup()
    led_clear()

    led_activate(RGB_RED)
    time.sleep(2)
    led_deactivate(RGB_RED)

    led_activate(RGB_BLUE)
    time.sleep(2)
    led_deactivate(RGB_BLUE)

    led_activate(RGB_GREEN)
    time.sleep(2)
    led_deactivate(RGB_GREEN)

    led_activate(RGB_RED)
    led_activate(RGB_BLUE)
    led_activate(RGB_GREEN)
    time.sleep(3)
    led_clear()

    led_clear()
    GPIO.cleanup()
 
main()
