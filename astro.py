#!/usr/bin/python3
from sense_hat import SenseHat
import datetime
import time
import csv

lastread = datetime.datetime.now()
sampling_interval= 1

def read_data():
    sense = SenseHat()
    sense.set_imu_config(True, True, True) 
    global lastread
    lastread=datetime.datetime.now()
    humidity = sense.get_humidity()
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    orientation = sense.get_orientation()
    compass_raw = sense.get_compass_raw()
    gyroscope_raw = sense.get_gyroscope_raw()
    accelerometer_raw = sense.get_accelerometer_raw()
    data={'Humidity':humidity,'Temperature':temperature,'Pressure':pressure,'Orientation':orientation, 'Compass_Raw':compass_raw, 'Gyroscope_raw':gyroscope_raw, 'Accelerometer_raw':accelerometer_raw}
    return data

with open( "pitch_data.csv" , "a" ) as data_file:
    writer=csv.writer(data_file,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['humidity','temperature','pressure','pitch','roll','yaw','compass_x','compass_y','compass_z','gyroscope_x','gyroscope_y','gyroscope_z','accel_x','accel_y','accel_z','timestamp'])

    while True:
        timestamp=datetime.datetime.now()
    
        if (timestamp-lastread).total_seconds() > sampling_interval:        
            data=read_data()
            humidity=data['Humidity']
            temperature=str(data['Temperature'])
            pressure=str(data['Pressure'])
            orientation=data['Orientation']
            compass_raw=data['Compass_Raw']
            gyroscope_raw=data['Gyroscope_raw']
            accel_raw=data['Accelerometer_raw']
            writer.writerow([humidity,temperature,pressure,str(orientation['pitch']),str(orientation['roll']),str(orientation['yaw']),
                             str(compass_raw['x']),str(compass_raw['y']),str(compass_raw['x']),
                             str(gyroscope_raw['x']),str(gyroscope_raw['y']),str(gyroscope_raw['x']),
                             str(accel_raw['x']),str(accel_raw['y']),str(accel_raw['x']), str(timestamp)])
            data_file.flush()
            print(data)

        
            
            

    


    
