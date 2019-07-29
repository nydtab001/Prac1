#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: taboka nyadza
Student Number: NYDTAB001
Prac: Prac 1
Date: 24/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
from itertools import product
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set up buttons as input with pull down resistor
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
chan_list = (11,13,15) # board numbers of LEDS
GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, 0)
count = 0
values = list(map(list, product((0,1), (0,1), (0,1)))) #convert tuple to list of lists
def my_callback(channel): # callback function for incrementing when first button is pressed
    global count
    if count < 7:
        count +=1 #increment global variable count
        GPIO.output(11, values[count][0])
        GPIO.output(13, values[count][1])
        GPIO.output(15, values[count][2])
    else:
        count = 0 # return to 0 if max value is reached
        GPIO.output(11, values[count][0])
        GPIO.output(13, values[count][1])
        GPIO.output(15, values[count][2])

def my_callback2(channel): # callback function for decrementing when second button is pressed
     global count
     if count > 0:
         count -= 1 # decrement global variable count if count > 0
         GPIO.output(11, values[count][0])
         GPIO.output(13, values[count][1])
         GPIO.output(15, values[count][2])
     else:
         count = 7 # return to max value if 0 is reached
         GPIO.output(11, values[count][0])
         GPIO.output(13, values[count][1])
         GPIO.output(15, values[count][2])

GPIO.add_event_detect(29, GPIO.RISING, callback=my_callback, bouncetime=100) # detect for first button press and call incrementing function if pressed
GPIO.add_event_detect(31, GPIO.RISING, callback=my_callback2, bouncetime=100) # detect for second button press and call decrementing function if pressed
# Logic that you write
def main():
    print("enter code here")
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
