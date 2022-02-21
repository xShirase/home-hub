pm2 start /home/g/pythondev/home/app.js
# pm2 start /home/g/pythondev/home/web/quote.js
python /home/g/pythondev/home/garden/sensors/heartbeat.py &!
python /home/g/pythondev/home/garden/sensors/motion.py &!
python /home/g/pythondev/home/garden/sensors/dht11.py &!
python /home/g/pythondev/home/garden/sensors/ds18b20.py &!
python /home/g/pythondev/home/garden/sensors/joystick.py &!
python /home/g/pythondev/home/garden/motors/motor.py &!
