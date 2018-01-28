#!/usr/bin/python3
from sense_hat import SenseHat
import datetime
import time
import csv
import threading
import astro_display
import astro_cabin_alt

#main data logging program
#collects data from IMU and Environmental sensors
#each sample written to line in .csv file with timestamp and status of LED Matrix
#Environmental data collected will be compared with data collected from Boeing 777 during team's visit to Gatwick airport
#IMU data will be used to generate waveforms for use in a wavetable oscillator to create a musical interpretation of this data

#coded by Cerys, Harrison and James


lastread = datetime.datetime.now()
sampling_interval= 1

def setup():
    with open( "sc_astro_data.csv" , "a" ) as data_file:
        writer=csv.writer(data_file,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['humidity','temperature','pressure','pitch','roll','yaw','compass_x','compass_y','compass_z','gyroscope_x','gyroscope_y','gyroscope_z','accel_x','accel_y','accel_z','timestamp','alt_display_active'])


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


def log():
    with open( "sc_astro_data.csv" , "a" ) as data_file:
        writer=csv.writer(data_file,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        
        data=read_data()
        humidity=data['Humidity']
        temperature=str(data['Temperature'])
        pressure=str(data['Pressure'])
        orientation=data['Orientation']
        compass_raw=data['Compass_Raw']
        gyroscope_raw=data['Gyroscope_raw']
        accel_raw=data['Accelerometer_raw']
        timestamp=datetime.datetime.now()
        writer.writerow([humidity,temperature,pressure,str(orientation['pitch']),str(orientation['roll']),str(orientation['yaw']),
                    str(compass_raw['x']),str(compass_raw['y']),str(compass_raw['x']),
                    str(gyroscope_raw['x']),str(gyroscope_raw['y']),str(gyroscope_raw['x']),
                    str(accel_raw['x']),str(accel_raw['y']),str(accel_raw['x']), str(timestamp),astro_cabin_alt.displaying])
        data_file.flush()

        if astro_cabin_alt.displaying==False:
            astro_display.updateDisplay()
            
        print('alt_display_active: '+str(astro_cabin_alt.displaying))
        print(data)
        print(" ")

        threading.Timer(sampling_interval, log).start()

        
            
            

    


    
