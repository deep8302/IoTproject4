import RPi.GPIO as rp
import time
rp.setwarnings(False)
l=[12,16,18,22,32,36]
rp.setmode(rp.BOARD)
for i in range(0,len(l)):
    rp.setup(l[i],rp.OUT)
li='WELCOME'
def clear():
    cmd(0x01)
    time.sleep(0.001)

def init():
    cmd(0x02)
    cmd(0x28)
    cmd(0x06)
    cmd(0x0C)
    cmd(0xC1)
    for i in range(0,len(li)):
        data(ord(li[i]))
        time.sleep(2)
    clear()

def cmd(c):
    d=c&0xF0
    d=d+0x02
    checkd(d)
    d=d-0x02
    checkd(d)
    d=(c<<4)&0xF0
    d=d+0x02
    checkd(d)
    d=d-0x02
    checkd(d)

def checkd(c):
    if((c&0x01)==0):
        rp.output(12,0)
    else:
        rp.output(12,1)
        
    if((c&0x02)==0):
        rp.output(16,0)
    else:
        rp.output(16,1)
        
    if((c&0x10)==0):
        rp.output(18,0)
    else:
        rp.output(18,1)
        
    if((c&0x20)==0):
        rp.output(22,0)
    else:
        rp.output(22,1)
        
    if((c&0x40)==0):
        rp.output(32,0)
    else:
        rp.output(32,1)
        
    if((c&0x80)==0):
        rp.output(36,0)
    else:
        rp.output(36,1)

def data(c):
    d=c&0xF0
    d=d+0x03
    checkd(d)
    d=d-0x02
    checkd(d)
    d=(c<<4)&0xF0
    d=d+0x03
    checkd(d)
    d=d-0x02
    checkd(d)
