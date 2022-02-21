#!/usr/bin/python
from i2cDriver import MotorDriver
import socketio
import time


sio = socketio.Client()
Motor = MotorDriver()
sio.connect('http://localhost:3000')


@sio.event
def startPump(data):
    Motor.MotorRun(0, 'fw', 100)
    time.sleep(2)
    Motor.MotorRun(0, 'bk', 100)
    time.sleep(2)
    Motor.MotorStop(0)


@sio.event
def stopPump(data):
  Motor.MotorStop(0)

while 1:
    pass