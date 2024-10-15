import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class DebouncedButton():
  def __init__(self, pin):
    self.pin = pin
    self.last_press = 0
    GPIO.setup(pin, GPIO.IN)

  def is_pressed(self):
    if not GPIO.input(self.pin) and time.time() - self.last_press > 0.7:
      self.last_press = time.time()
      return True
    else:
      return False

class LED():
  def __init__(self, pin):
    self.pin = pin
    GPIO.setup(self.pin,GPIO.OUT)

  def on(self):
    GPIO.output(self.pin,1)

  def off(self):
    GPIO.output(self.pin,0)
