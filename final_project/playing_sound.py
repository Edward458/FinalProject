import os
# import required libraries
from pydub import AudioSegment 
from pydub.playback import play 

def play_audio(song):
    os.chdir("songs")

    for song in os.listdir():
        sound = AudioSegment.from_mp3('Wavestep.mp3')
        play(sound)