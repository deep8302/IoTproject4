import RPi.GPIO as io
io.setwarnings(False)
import sys as s
import Adafruit_DHT as ad
io.setmode(io.BOARD)
import time
import firebrigade
io.setup(11,io.IN)
io.setup(19,io.IN)
io.setup(29,io.IN)
def Parking():
    count=10
    
    if(io.input(11)):
        if(count!=0):
            print("vehicle entered")
            count=count-1
            print("aval space",count)
        
    elif(io.input(19)):
        print("vehicle departed")
        count=count+1
        print("aval space",count)
        
        
   if(count==0):
       print("no space availaible")
       continue
       time.sleep(1)
    
def Temp():
    
    hum,temp=ad.read_retry(11,5)
    print(hum,' ',temp)
    time.sleep(1)
    if(temp > 70 ):
        print('fire alert ')
        firebrigade.fire()
        time.sleep(2)
