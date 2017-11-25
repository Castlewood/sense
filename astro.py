#!/usr/bin/python3
from sense_hat import SenseHat
import datetime
import time
import csv

lastread = datetime.datetime.now()

def read_data():
    sense = SenseHat()
    global lastread
    lastread=datetime.datetime.now()
    o = sense.get_orientation()
    return o

while True:
    timestamp=datetime.datetime.now()
    
    if (timestamp-lastread).total_seconds() > 10:        
        data=read_data()
        print(data)

        with open( "pitch_data.csv" , "a" ) as f:
            writer=csv.writer(f,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
            writer.writerow([str(data['pitch']),str(data['roll']),str(data['yaw']), str(timestamp)])
            

    


    
