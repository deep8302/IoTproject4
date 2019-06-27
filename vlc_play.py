import vlc
import time
instance=vlc.Instance()
player=instance.media_player_new()
media=instance.media_new('C:/Users/dell/Desktop/SMART CITY/trial.mp3')
media.get_mrl()
player.set_media(media)
player.play()



