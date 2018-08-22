#!/usr/bin/python
import RPi.GPIO as GPIO
import time

red=0
yellow=1
green=2
f_red=3
f_green=4
taste=5
Ampel=[18,23,24,25,8,7]

GPIO.setmode(GPIO.BCM)
GPIO.setup(Ampel[red], GPIO.OUT,initial=0)
GPIO.setup(Ampel[yellow], GPIO.OUT,initial=0)
GPIO.setup(Ampel[green], GPIO.OUT,initial=1)
GPIO.setup(Ampel[f_red], GPIO.OUT,initial=1)
GPIO.setup(Ampel[f_green], GPIO.OUT,initial=0)
GPIO.setup(Ampel[taste], GPIO.IN)

print("press the button to turn on the pedestrian light. Ctrl+C terminate the program.")
try:
    while True:
        if GPIO.input(Ampel[taste])==1:
            GPIO.output(Ampel[green],0)
            GPIO.output(Ampel[yellow],1)
            time.sleep(0.6)
            GPIO.output(Ampel[yellow],0)
            GPIO.output(Ampel[red],1)
            time.sleep(0.6)
            GPIO.output(Ampel[f_red],0)
            GPIO.output(Ampel[f_green],1)
            time.sleep(2)
            GPIO.output(Ampel[f_green],0)
            GPIO.output(Ampel[f_red],1)
            time.sleep(0.6)
            GPIO.output(Ampel[yellow],1)
            time.sleep(0.6)
            GPIO.output(Ampel[red],0)
            GPIO.output(Ampel[yellow],0)
            GPIO.output(Ampel[green],1)
            time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
