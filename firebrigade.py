import RPi.GPIO as rp
import time as t
i=0
rp.setmode(rp.BOARD)
rp.setwarnings(False)
rp.setup(38,rp.OUT)
while(i<10):
    rp.output(38,1)
    t.sleep(1)
    rp.output(38,0)
    t.sleep(1)
    i=i+1
