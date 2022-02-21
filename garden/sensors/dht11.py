from time import sleep
import Adafruit_DHT
import socketio

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 26

def updateDHT():
    while running:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            sio.emit('input', {'type':'dht', 't': int(temperature), 'h': int(humidity)})
        sleep(5)


sio = socketio.Client()
sio.connect('http://localhost:3000')

running = True
try:
    print('DHT Started')
    updateDHT()
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    running = False
    print('DHT Stopped')
    sleep(1)

