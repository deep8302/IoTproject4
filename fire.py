import vlc
import time as t
i=0
while(i<5):
    instance=vlc.Instance()
    player=instance.media_player_new()
    ch='/home/pi/Desktop/SMART CITY/fire.mp3'
    media=instance.media_new(ch)
    media.get_mrl()
    player.set_media(media)
    player.audio_set_volume(1000)
    player.play()
    i=i+1
    t.sleep(1)
    
