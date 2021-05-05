import mutagen
import re
from Song import Song
from Playlist import Playlist
from functions import *
import os
from playing_sound import *

# when the program begins scan the songs folder

# create the user_library dictionary
user_library = dict()

# now assign all the song metadata
# change the folder into the songs folder

os.chdir("songs")
# iterate through the folder assigning the approriate metadata
for song in os.listdir():
   # the song title is the key, the value is a list with
    user_library[get_song_metadata(song)[1]] = (get_song_metadata(song)[2], Song(get_song_metadata(song)[0], get_song_metadata(song)[1], get_song_metadata(song)[2], get_song_metadata(song)[3], get_song_metadata(song)[4], get_song_metadata(song)[5]))

# show the user the library
for key, value in user_library.items():
    print(key + "-" + value[0])

print("---------------------------------------------------------")

print(view_info(user_library["Wavestep"][1]))


# MUST BE ADDED

# play:[song]
    

# IF I HAVE TIME 
# edit: [playlist]
# remove: [playlist]
# create: [playlist]