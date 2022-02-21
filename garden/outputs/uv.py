from time import sleep
import logging

#### Remote codes
PROTOCOL = 1
PULSE = 385
ON =  5592321
OFF = 5592323
BRIGHT = 5592324
DIM = 5592326
TOGGLE = 5592329
HFOUR = 5592333
HEIGHT = 5592335
HTWELVE = 5592336
CXL = 5592338

from rpi_rf import RFDevice
logging.basicConfig(
  level=logging.INFO,
  datefmt='%Y-%m-%d %H:%M:%S',
  format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)


def sendCode(code):
  logging.info("Sending " + str(code))
  rfdevice.tx_code(code, PROTOCOL, PULSE)



rfdevice = RFDevice(17) # GPIO Tx pin
rfdevice.enable_tx()

sendCode(ON)
sleep(5)
sendCode(TOGGLE)
# sleep(1)
# sendCode(TOGGLE)
# sleep(1)
# sendCode(TOGGLE)
# sleep(1)
# sendCode(TOGGLE)
# sleep(1)
# sendCode(TOGGLE)
# sleep(1)
# sendCode(TOGGLE)
# sleep(1)
# sendCode(TOGGLE)
# sleep(1)
# sendCode(TOGGLE)
sleep(1)
sendCode(OFF)
sleep(1)

rfdevice.cleanup()
