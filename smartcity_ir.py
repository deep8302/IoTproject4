import RPi.GPIO as rp
import time as t
i=0
rp.setmode(rp.BOARD)
rp.setwarnings(False)
rp.setup(7,rp.IN)
rp.setup(40,rp.OUT)
while(i<10):
    if(rp.input(7)==1):
        rp.output(40,1)
        t.sleep(2)
        rp.output(40,0)
        t.sleep(2)
        i=i+1
        
