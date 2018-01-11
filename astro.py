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
    orientation = sense.get_orientation()
    compass_raw = sense.get_compass_raw()
    accelerometer_raw = sense.get_accelerometer_raw()
    data={'Orientation':orientation, 'Compass_Raw':compass_raw, 'Accelerometer_raw':accelerometer_raw}
    return data

with open( "pitch_data.csv" , "a" ) as data_file:
    writer=csv.writer(data_file,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['pitch','roll','yaw','mag_x','mag_y','mag_z','accel_x','accel_y','accel_z','timestamp'])

    while True:
        timestamp=datetime.datetime.now()
    
        if (timestamp-lastread).total_seconds() > sampling_interval:        
            data=read_data()
            orientation=data['Orientation']
            compass_raw=data['Compass_Raw']
            accel_raw=data['Accelerometer_raw']
            writer.writerow([str(orientation['pitch']),str(orientation['roll']),str(orientation['yaw']),
                             str(compass_raw['x']),str(compass_raw['y']),str(compass_raw['x']),
                             str(accel_raw['x']),str(accel_raw['y']),str(accel_raw['x']), str(timestamp)])
            data_file.flush()
            print(data)

        
            
            

    


    
