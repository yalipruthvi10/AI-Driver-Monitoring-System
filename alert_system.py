import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

def alert():
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(buzzer, GPIO.LOW)