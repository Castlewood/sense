#!/usr/bin/python3
from sense_hat import SenseHat
import threading
import astro_display

#calculate and display cabin altitude each time orbit display increments
#if cabin alt less than B777 "Cabin Alt" warning limit display in green text
#if cabin alt greater than B777 "Cabin Alt" warning limit display in red text

#coded by Holly

displaying = False

def display_cabin_alt():
    sampling_interval=astro_display.orbitPosIncrementSeconds
    
    global displaying
    displaying=True
    sense = SenseHat()
    current_pixels=sense.get_pixels()
    sense.clear()
    p=sense.get_pressure()
    a=(1-(p/1013.25)**0.190284)*145366.45
    alt=int(round(a))

    if alt > 9999:
        c = [255, 0, 0]
    else:
        c = [0, 255, 0]
    
    sense.show_message("Cabin Alt: "+str(alt)+"ft", text_colour=c)
    displaying=False
    sense.set_pixels(current_pixels)
    threading.Timer(sampling_interval, display_cabin_alt).start()
    
