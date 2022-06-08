import time,sys
sys.path.append('../')
# load AMG8833 module
import amg8833_i2c
import numpy as np
from time import sleep

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
print ("Socket successfully created")
port = 12346 
s.bind(('', port))        
print ("socket binded to %s" %(port))
s.listen(5)    
print ("socket is listening")

t0 = time.time()
sensor = []

while (time.time()-t0)<1: # wait 1sec for sensor to start
    try:
        # AD0 = GND, addr = 0x68 | AD0 = 5V, addr = 0x69
        sensor = amg8833_i2c.AMG8833(addr=0x69) # start AMG8833
    except:
        sensor = amg8833_i2c.AMG8833(addr=0x68)
    finally:
        pass
time.sleep(0.1) # wait for sensor to settle

# If no device is found, exit the script
if sensor==[]:
    print("No AMG8833 Found - Check Your Wiring")
    sys.exit(); # exit the app if AMG88xx is not found 


pix_to_read = 64 # read all 64 pixels
while True:
    conn, addr = s.accept()
    print ('Client connection accepted: ', addr)
    while True:
        try:
            status,pixels = sensor.read_temp(pix_to_read) # read pixels with status
            if status: # if error in pixel, re-enter loop and try again
                continue
            pixels=str(pixels)
            data=pixels
            print ('Server sent:', data)
            conn.send(data.encode()) 
            time.sleep(1)
        except (socket.error, msg):
            print ('Client connection closed: ', addr)
            break

conn.close()
