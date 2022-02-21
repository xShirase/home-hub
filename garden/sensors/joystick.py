from time import sleep
import Adafruit_MCP3008
import socketio

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
sio = socketio.Client()
sio.connect('http://localhost:3000')
air = 570
wet = 210

print('Started Soil Monitors & Pump')
while True:
    joyBtn = mcp.read_adc(3)

    if joyBtn == 0:
        sio.emit('input', { 'type':'startPump' })

    pot1 = mcp.read_adc(0)
    pot2 = mcp.read_adc(4)
    v1 = int((100*(air-pot1)/(air-wet)))
    v2 = int(100*((air-pot2)/(air-wet)))

    sio.emit('input', { 'type':'plants', 'data': str(v1)+'% '+str(v2)+'%'})

    sleep(5)
