from time import sleep
import socketio

def heartbeat():
    while running:
        sio.emit('input', { 'body': u'\x05', 'type':'heart'})
        sleep(0.5)
        sio.emit('input', { 'body': u'\x06', 'type':'heart'})
        sleep(0.5)

sio = socketio.Client()
sio.connect('http://localhost:3000')

running = True
try:
    print('Heartbeat Started')
    heartbeat()
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    running = False
    print('Heartbeat Stopped')
