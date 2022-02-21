from RPLCD import CharLCD
import RPi.GPIO as GPIO
from time import sleep
import queue
import signal
from threading import Thread
import socketio
from collections import deque

# PINS
RS_PIN = 21
E_PIN = 20
D4_PIN = 19
D5_PIN = 13
D6_PIN = 6
D7_PIN = 5
PIR_PIN = 12

SMILEY = (0b00000, 0b01010, 0b01010, 0b00000, 0b10001, 0b10001, 0b01110, 0b00000)
PENIS = (0b00100, 0b001010, 0b01110, 0b01010, 0b01010, 0b10001, 0b10101, 0b01010)
HEART = (0b00000, 0b00000, 0b01010, 0b10101,  0b10001, 0b01010, 0b00100, 0b00000)
HEART2 = (0b00000, 0b00000, 0b01010, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000)
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=RS_PIN,
      pin_e=E_PIN, pins_data=[D4_PIN, D5_PIN, D6_PIN, D7_PIN])


def initLCD():
  lcd.clear()
  lcd.create_char(3, SMILEY)
  lcd.create_char(4, PENIS)
  lcd.create_char(5, HEART)
  lcd.create_char(6, HEART2)
  lcd.cursor_mode = 'hide'


class Message:
  def __init__(self, y, x, body):
    self.x = x
    self.y = y
    self.body = body

dq = deque()

def processLongMessage(x,y,body):
  l = len(body)-16
  for i in range(l):
    s = body[0+i:16+i]
    dq.append(Message(y, x, s))
    sleep(.5)


def worker():
  while True:
    try:
      item: Message = dq.popleft()
      if str(item) != '':
        if len(item.body) > 16:
          print('too long')
          processor = Thread(target=processLongMessage, args=(item.x,item.y,item.body,))
          processor.start()
        else:
          write(item)
    except IndexError:
      pass


def write(m):
  lcd.cursor_pos = (m.y, m.x)
  lcd.write_string(m.body)


sio = socketio.Client()

@sio.event
def clock(data):
  dq.append(Message(0, 8, data))


@sio.event
def dht(data):
  dq.append(Message(0, 0, str(data['t'])+'C'))
  dq.append(Message(0, 4, str(data['h'])+'%'))


@sio.event
def heart(data):
  dq.append(Message(0, 15, data['body']))
  dq.append('')


@sio.event
def motion(d):
  dq.append(Message(0, 14, '\x03'))


@sio.event
def noMotion(d):
  sleep(2)
  dq.append(Message(0, 14, ' '))


running = True
try:
  tq = Thread(target=worker, daemon=True)
  tq.start()
  initLCD()
  sio.connect('http://localhost:3000')
  signal.pause()
except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
  running = False
  sio.disconnect()
  dq.clear()
  print('Clearing LCD/GPIO')
  lcd.clear()
  sleep(5)
