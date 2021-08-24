#!/usr/bin/python
#coding:utf8

import sys
import time
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')
import RPi.GPIO as GPIO

def cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
        return float(f.read())/1000

def main():
    GPIO_FANS = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_FANS, GPIO.OUT, initial=GPIO.HIGH)

    is_close = True
    while True:
        temp = cpu_temp()
        if is_close:
            if temp > 45.0:
                GPIO.output(GPIO_FANS, GPIO.HIGH)
                is_close = False
        else:
            if temp < 42.0:
                GPIO.output(GPIO_FANS, GPIO.LOW)
                is_close = True

        time.sleep(10.0)
        print temp

if __name__ == '__main__':
    main()