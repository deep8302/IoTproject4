
import requests
import os
import gtts
import time as t
def text_speak(text):
    
    mytext = text
    language = 'en'
    file= gtts.gTTS(text=mytext, lang=language, slow=False)
    print(file)
    file.save("call.mp3")
    os.startfile("call.mp3")

while(1):
    i=0
    r=requests.get('http://indianiotcloud.com/retrieve.php?id=NQUEES7HH78J9XVFDN29')
    d=r.json()
    print(d)
    d1=d['result'][0]['field1']
    d2=d['result'][0]['field2']
    while(i<3):
        if(len(d1)>0):
            text='HELLO '+str(d1)+' YOUR MOM '+str(d2)+'IS CALLING YOU PLEASE GO'
            text_speak(text)
            t.sleep(7)
        i=i+1
