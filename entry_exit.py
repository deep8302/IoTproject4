import serial
import xlwt as xw
import xlrd as xr
import time as t
import smtplib as sm
import RPi.GPIO as rp
rp.setwarnings(False)
rp.setmode(rp.BOARD)
rp.setup(7,rp.OUT)


wbr=xr.open_workbook('Book1.xls')
shr=wbr.sheet_by_index(0)
dname=shr.col_values(0)
dcar_id=shr.col_values(1)
demail=shr.col_values(2)
dstatus=shr.col_values(3)
dlist=[dname,dcar_id,demail,dstatus]
nc=shr.ncols
wb=xw.Workbook()
shw=wb.add_sheet('sheet1',cell_overwrite_ok=True)
    


def entry(loc):
    print('\nWELCOME:',dname[loc])
    for i in range(0,nc):
        for j in range(0,nc):
            shw.write(i,j,dlist[j][i])
    shw.write(loc,3,'1')
    wb.save('Book1.xls')
    #rp.output(7,1)

def mail(loc,ch):
    m=sm.SMTP('smtp.gmail.com',587)
    m.starttls()
    id='destrothedestroyeer@gmail.com'
    receiver_id=demail[loc]
    data='YOU JUST '+str(ch)+' SMART CITY'
    m.login(id,'destro_14')
    m.sendmail(id,receiver_id,data)
    print('A MAIL IS SENT TO YOUR REGISTERED EMAIL ID\n')
    m.close()

    

while(1):
    flag=-1
    s=serial.Serial('/dev/ttyUSB0')
    s.close()
    s.open()
    print('PLEASE SWIPE YOUR CARD')
    number=s.read(12)
    number=number.decode('utf-8')
    for i in range(1,len(dcar_id)):
        if(number==dcar_id[i]):
            
            flag=i
            import welcome
    if(flag>-1):
       print('CARD ACCEPTED\nPROCESSING PLEASE WAIT',end='')
       for i in range(0,3):
           t.sleep(1)
           print('.',end='')
       if(dstatus[flag]=='0'):
            entry(flag)
            mail(flag,'ENTERED')
       if(dstatus[flag]=='1'):
           import eexit
           dstatus[flag]='0'
           print('THANK YOU',dname[flag],'FOR THE VISIT')
           shw.write(flag,3,'0')
           mail(flag,'EXIT')
           t.sleep(1)
    else:
        print('NEW CARD DETECTED\n')
        import welcome
