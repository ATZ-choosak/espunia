import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Poten():
  def __init__(self, pin):
    self.pin = pin
    GPIO.setup(pin, GPIO.IN)

  def value(self):
	  return GPIO.input(self.pin)
