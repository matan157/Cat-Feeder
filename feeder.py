"""
    Cat Feeder by Matan Uchen

    This program will be the logic for an automatic cat feeder.
    Feeder was made using a snack dispenser and servo, powered by batteries
    and my mind.

"""
from gpiozero import Button
import RPi.GPIO as GPIO
import time

servoPin = 21 # Pin powering sending signal to servo.
feedTime = 5 # How long it should rotate. (Seconds)
startTime = 0 # When the program starts.

b = Button(4)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
servo = GPIO.PWM(servoPin, 50)

def feed():
    servo.start(2.5)
    time.sleep(feedTime)
    servo.stop()
feed()
b.when_pressed = feed
b.when_released = servo.stop()
try:
    while True:
        if startTime == 0:
            feed()
            startTime = time.time()
        elapsedTime = time.time() - startTime
        if elapsedTime >= 86400:
            feed()
    time.sleep(.1)

except:
    servo.stop()
    GPIO.cleanup()

