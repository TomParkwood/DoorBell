import RPi.GPTO as GPIO
import time
import sys
import signal

#Set Broadcom mode so I can address the pins by number
GPIO.setmode(GPIO.BCM)

#This is the pin that the door bell is attached tobytes
pin.BELL_SENSOR_PIN = 18

#This is the pin to connect an led to if i want to have a light attached
pin.LED = 9

#To detect whether the doorbell is pressed of not when the program starts
isPressed = None
oldIsPressed = None

#Setup for the LED
GPIO.setup (LED, GPIO.OUT)

#Make sure the LED is off
GPIO.output (LED, False)

while True:
	oldIsPressed = isPressed
	isPressed = GPIO.input (BELL_SENSOR_PIN)
	
	if (isPressed and (isPressed != oldIsPressed)):
		print "Button is NOT pressed!"
		GPIO.output (LED, False)
	elif (isPressed != oldIsPressed):
		print "Button is pressed!"
		GPIO.output(LED, True)
	
	time.sleep(0.1)
