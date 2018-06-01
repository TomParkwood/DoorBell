import RPi.GPTO as GPIO
import time
import sys
import signal
from pushbullet import Pushbullet

#Setup pushbullet api
pb = Pushbullet(o.ZK6aX17EHbDTYc7PzmXFBC9OdCGDsEgE)

#Set Broadcom mode so I can address the pins by number
GPIO.setmode(GPIO.BCM)

#This is the pin that the door bell is attached tobytes
pin.BELL_SENSOR_PIN = 18

#This is the pin to connect an led to if i want to have a light attached
pin.LED = 9

#To detect whether the doorbell is pressed of not when the program starts
isPressed = None
oldIsPressed = None

#Clean up when the user exits with the keyboard, this makes sure the led is turned off
def cleanupLED(signal, frame):
	GPIO.output(LED, False)
	GPIO.cleanup()
	sys.exit(0)
	
#Setup for the switch
#Not too sure of this, in the example this is because the switch only uses 1 pin and ground so he has a pull up resistor to stop the pin from floating.
GPIO.setup (BELL_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Setup for the LED
GPIO.setup (LED, GPIO.OUT)

#Make sure the LED is off
GPIO.output (LED, False)

#Clean the lights when it is exited using Ctrl-C to exit
signal.signal(signal.SIGINT, cleanupLED)

#Actual code which checks to see if the button has been pressed.
while True:
	oldIsPressed = isPressed
	isPressed = GPIO.input (BELL_SENSOR_PIN)
	
	if (isPressed and (isPressed != oldIsPressed)):
		print "Button is NOT pressed!"
		GPIO.output (LED, False)
	elif (isPressed != oldIsPressed):
		print "Button is pressed!"
		GPIO.output(LED, True)
		#First test using just the led and the print to screen so i can test the notifications seperately
		#push = pb.push_note("Doorbell", "The doorbell has been pressed at unit 9 @" & print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
		#sleep for 2 seconds so if there is ripple from the switch then it wont send out multiple notifications.
		time.sleep(2)
		
	time.sleep(0.1)
