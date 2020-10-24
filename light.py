#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example. Showcases
# various animations on a strip of NeoPixels.
 
import time
from neopixel import *
import argparse
import psutil
 
COLOR = [0,30,255]
# LED strip configuration:
LED_COUNT = 12 # Number of LED pixels.
LED_PIN = 18 # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN = 10 # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10 # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0 # set to '1' for GPIOs 13, 19, 41, 45 or 53
 
def mix(color, strength):
    return Color(int(color[0] * strength), int(color[1] * strength), int(color[2] * strength))

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
pos = 0.0
load = 0
while True:
    rawLoad = psutil.cpu_percent(interval=0.01) / 100
    load = load + (rawLoad - load) * 0.01
    #print(load)
    loadFac = 0.2 + load*0.8
    for i in range(LED_COUNT):
        strength = abs(i - pos) / LED_COUNT
        if strength < 0.5:
            strength = 1 - strength
        strength = pow(strength, 2) - 0.4
        if strength<0:
            strength = 0
        strength *= loadFac
        strip.setPixelColor(i, mix(COLOR, strength))
    pos += 0.1 * loadFac
    if pos >= LED_COUNT:
        pos = 0.0
    strip.show()
