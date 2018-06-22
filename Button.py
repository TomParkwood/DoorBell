import RPi.GPIO as GPIO
import time
import requests

#setup the GPIO pins, they need to be in BCM mode whatever that is
#6 is the button, this has a pull up resistor
#21 is the LED which is configured to be an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.OUT)

#at the start of the program make sure the LED is off
GPIO.output(21,False)

while True:
	#Get whether or not th button is pressed
	inputValue = GPIO.input(6)
	#if the button is pressed then execute these commands
	if (inputValue == False):
		#This was for testing it writes button pressed onto the command line
		#print("Button pressed ")
		#Set the LED to high
		GPIO.output(21,True)
		#This is the curl command stripped down to python so it can be executed
		data = [
				('devid', 'v299F4B9B4FBFA3E'),
				]
		response = requests.post('http://api.pushingbox.com/pushingbox', data=data)
		#So there isnt a spam of notifications, this will wait 1 second to see if the button is pressed again
		time.sleep(1)
		#after a second turn the led off, if they are still holding the button then the LED will light again
		GPIO.output(21, False)
	#So it will wait .3 seconds after the code has been executed to see if the button is still pressed, helps with button ripple
	time.sleep(0.3)
	
#To change the doorbell sound, use the chrome extension, and download the contents of the extension
#extract it and then change the alert.ogg file, you could change the notifier.js file and change the pb.alertsound to the file you want it to play.
#On chrome you need to go settings, more tools, then extensions. Enable developer mode.
#Load unpacked extension up the top and select the folder for the extension.
#Make sure that in the extension settings under the options then notifications to enable the play a sound when a notification arrives.
#Test, it should make the doorbell sound when a notification is recieved.