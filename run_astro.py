#!/usr/bin/python3
import datetime
import numpy as np
import time
from random import randint
import sys
import threading
from sense_hat import SenseHat
sense = SenseHat()

import astro

#global vars

b = (0, 0, 255) # Blue
g = (0, 255, 0) # Green
o = (0, 0, 0) # Black
w = (255, 255, 255) # White
r = (255, 0, 0) # Red
y = (255, 255, 0) # Yellow
p = (255, 125, 125) # pink

orbitPos = 0
secondOrbit = 0
orbitPosIncrementSeconds = 270 #change to 270 for 4.5 minutes per pixel increment for orbit (4.5x20 = 90 minutes)

#functions

def drawScreen():
  
  image = [
   o, o, w, w, w, w, o, o,
   o, b, b, b, b, b, b, o,
   b, b, g, g, g, g, b, b,
   b, g, g, g, g, g, b, b,
   b, b, g, g, g, b, g, b,
   b, b, g, g, b, g, g, b,
   o, b, b, g, b, b, b, o,
   o, o, b, w, w, b, o, o
  ]
  sense.set_pixels(image)
  sense.rotation = 180

def flashPixel():
  now = datetime.datetime.now()
  seconds = now.second #% 60
  if seconds % 2 == 0:
    sense.set_pixel(7, 7, y)
  else:
    sense.set_pixel(7, 7, o)

def moveISS():
  global orbitPos
  global secondOrbit
   
  if secondOrbit == 0:
    tailColour = p
  else:
    tailColour = y
    
  if orbitPos == 1:
    sense.set_pixel(0, 4, tailColour)
    sense.set_pixel(0, 5, r)
  if orbitPos == 2:
    sense.set_pixel(0, 5, tailColour)
    sense.set_pixel(1, 6, r)
  if orbitPos == 3:
    sense.set_pixel(1, 6, tailColour)
    sense.set_pixel(2, 7, r)
  if orbitPos == 4:
    sense.set_pixel(2, 7, tailColour)
    sense.set_pixel(3, 7, r)
  if orbitPos == 5:
    sense.set_pixel(3, 7, tailColour)
    sense.set_pixel(4, 7, r)
  if orbitPos == 6:
    sense.set_pixel(4, 7, tailColour)
    sense.set_pixel(5, 7, r)
  if orbitPos == 7:
    sense.set_pixel(5, 7, tailColour)
    sense.set_pixel(6, 6, r)
  if orbitPos == 8:
    sense.set_pixel(6, 6, tailColour)
    sense.set_pixel(7, 5, r)
  if orbitPos == 9:
    sense.set_pixel(7, 5, tailColour)
    sense.set_pixel(7, 4, r)
  if orbitPos == 10:
    sense.set_pixel(7, 4, tailColour)
    sense.set_pixel(7, 3, r)
  if orbitPos == 11:
    sense.set_pixel(7, 3, tailColour)
    sense.set_pixel(7, 2, r)
  if orbitPos == 12:
    sense.set_pixel(7, 2, tailColour)
    sense.set_pixel(6, 1, r)
  if orbitPos == 13:
    sense.set_pixel(6, 1, tailColour)
    sense.set_pixel(5, 0, r)
  if orbitPos == 14:
    sense.set_pixel(5, 0, tailColour)
    sense.set_pixel(4, 0, r)
  if orbitPos == 15:
    sense.set_pixel(4, 0, tailColour)
    sense.set_pixel(3, 0, r)
  if orbitPos == 16:
    sense.set_pixel(3, 0, tailColour)
    sense.set_pixel(2, 0, r)
  if orbitPos == 17:
    sense.set_pixel(2, 0, tailColour)
    sense.set_pixel(1, 1, r)
  if orbitPos == 18:
    sense.set_pixel(1, 1, tailColour)
    sense.set_pixel(0, 2, r)
  if orbitPos == 19:
    sense.set_pixel(0, 2, tailColour)
    sense.set_pixel(0, 3, r)
  if orbitPos == 20:
    sense.set_pixel(0, 3, tailColour)
    sense.set_pixel(0, 4, r)
    
def updateDisplay():
  flashPixel()
  moveISS()
  threading.Timer(0.9, updateDisplay).start()

def incrementOrbitPos():
  global orbitPos
  global secondOrbit
  global orbitPosIncrementSeconds
  if orbitPos == 20:
    if secondOrbit == 0:
      secondOrbit = 1
    else:
      secondOrbit = 0
    orbitPos = 0
  else:
    orbitPos = orbitPos + 1
  threading.Timer(orbitPosIncrementSeconds, incrementOrbitPos).start()

#main program
drawScreen()
incrementOrbitPos()
updateDisplay()
astro.log()
