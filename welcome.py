import vlc
instance=vlc.Instance()
player=instance.media_player_new()
ch='/home/pi/Desktop/SMART CITY/trial.mp3'
media=instance.media_new(ch)
media.get_mrl()
player.set_media(media)
player.audio_set_volume(10000)
player.play()



