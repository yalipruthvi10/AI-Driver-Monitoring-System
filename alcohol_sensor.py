import RPi.GPIO as GPIO
import time

sensor = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

while True:
    if GPIO.input(sensor):
        print("Alcohol Detected!")
    else:
        print("Safe")
    time.sleep(1)