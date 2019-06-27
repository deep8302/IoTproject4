import time as t
c=input(('PRESS SPACE TO ENTER THE CITY'))
if(c==' '):
      ch=int(input('WHAT WOULD YOU LIKE TO DO\n1.WANT TO ENTER THE BUILDING\n2.WANT TO ENTER THE FACTORY\n3.MAKE ANNOUNCEMENT IN PLAYGROUND\n4.HOSPITAL STATUS\n5.ROAD STATUS'))
      if(ch==1):
          import Building
          a=int(input('1.PARKING\n2.TEMPERATURE\n'))
                  if(a==1):
                      Building.parking()
                  else:
                      for i in range(0,10):
                          Building.Temp()
                          time.sleep(1)
      elif(ch==2):
          import factory
          factory.Factory()
      elif(ch==3):
          import playground
      elif(ch==4):
          import smartcity_ir
                      
