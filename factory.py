import RPi.GPIO as rp
import time as t
rp.setmode(rp.BOARD)
rp.setup(7,rp.IN)
rp.setup(31,rp.OUT)
rp.setup(33,rp.OUT)
rp.setwarnings(False)
c=0
while(1):
        if(rp.input(7)==1):
                rp.output(31,1)
                rp.ouput(33,0)
                t.sleep(1)
                rp.output(31,0)
                while(rp.input(7)):
                        pass
                c=c+1
                t.sleep(5)
                rp.output(31,0)
                rp.output(33,1)
                t.sleep(1)
                rp.output(33,0)
                
