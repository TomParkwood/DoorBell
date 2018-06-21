import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.OUT)

GPIO.output(21,False)

while True:
	inputValue = GPIO.input(6)
	if (inputValue == False):
		print("Button pressed ")
		GPIO.output(21,True)
		data = [
				('devid', 'v299F4B9B4FBFA3E'),
				]
		response = requests.post('http://api.pushingbox.com/pushingbox', data=data_
		time.sleep(1)
		GPIO.output(21, False)
	time.sleep(0.3)