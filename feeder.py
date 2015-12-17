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
startTime = time.time() # When the program starts.

b = Button(4) # Button on pin 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
servo = GPIO.PWM(servoPin, 50)

# Methon for when button is pressed. Feeds for indefinite amount of time.
def feedButton():
    servo.start(2.5)
    time.sleep(5)
# Stops the servo.
def stop():
    servo.stop()

# Feed method.
def feed():
    servo.start(2.5)
    time.sleep(feedTime)
    stop()

b.when_released = stop
try:
    while True:
        elapsedTime = time.time() - startTime
        if elapsedTime >= 86400 or b.is_pressed:
            feed()
            startTime = time.time()
    time.sleep(.1)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

