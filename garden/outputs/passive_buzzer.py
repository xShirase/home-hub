# Import required libraries
import sys
import RPi.GPIO as GPIO
import time

# Set trigger PIN according with your cabling
triggerPIN = 18

# Set PIN to output
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN,GPIO.OUT)

# define PWM signal and start it on trigger PIN
buzzer = GPIO.PWM(triggerPIN, 440) # Set frequency to 1 Khz
buzzer.start(10) # Set dutycycle to 10
time.sleep(1)
buzzer.ChangeFrequency(494) # Set frequency to 1 Khz
time.sleep(1)
buzzer.ChangeFrequency(523) # Set frequency to 1 Khz
time.sleep(1)
buzzer.ChangeFrequency(587) # Set frequency to 1 Khz
time.sleep(1)
buzzer.ChangeFrequency(659) # Set frequency to 1 Khz
time.sleep(1)
buzzer.ChangeFrequency(698) # Set frequency to 1 Khz
time.sleep(1)
buzzer.ChangeFrequency(784) # Set frequency to 1 Khz
time.sleep(1)





GPIO.cleanup()
sys.exit()

# Please find below some addictional commands to change frequency and
# dutycycle without stopping buzzer, or to stop buzzer:
#
# buzzer.ChangeDutyCycle(10)
# buzzer.ChangeFrequency(1000)
# buzzer.stop()
