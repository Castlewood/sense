#!/usr/bin/python3
from sense_hat import SenseHat
import datetime
import time
import csv

lastread = datetime.datetime.now()
sampling_interval= 1

def read_data():
    sense = SenseHat()
    global lastread
    lastread=datetime.datetime.now()
    o = sense.get_orientation()
    return o

with open( "pitch_data.csv" , "a" ) as data_file:
    writer=csv.writer(data_file,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['pitch','roll','yaw','timestamp'])

    while True:
        timestamp=datetime.datetime.now()
    
        if (timestamp-lastread).total_seconds() > sampling_interval:        
            data=read_data()        
            writer.writerow([str(data['pitch']),str(data['roll']),str(data['yaw']), str(timestamp)])
            data_file.flush()
            print(data)

        
            
            

    


    
