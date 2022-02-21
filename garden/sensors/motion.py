import RPi.GPIO as GPIO
from time import sleep
import socketio

PIR_PIN = 12

def initGPIO():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PIR_PIN, GPIO.IN)
  sleep(1)
  print('GPIO Ready')

def checkMotion():
  recent = False
  while running:
    if GPIO.input(PIR_PIN) and recent == False:
      sio.emit('input', {'type': 'motion'})
      recent = True
    elif GPIO.input(PIR_PIN):
      recent = True
    elif recent == True:
      sio.emit('input', {'type': 'noMotion'})
      recent = False
    sleep(.25)

initGPIO()

sio = socketio.Client()
sio.connect('http://localhost:3000')
running = True

try:
  print('PIR Started')
  checkMotion()
except BaseException:
  running = False
  print('PIR Stopped')
