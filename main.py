
'''
Edward Mesa
Professor Penta
Programing for IT
Final Project
May 5, 2021
'''


import mutagen
import re
from Song import Song
from functions import *
import os
from playsound import playsound
from pynput import keyboard

music_folder = None

folder = open("config.txt", "r")
for entry in folder:
    if entry.startswith("music_folder="):
        music_folder = str(re.findall("music_folder=(.+)", entry))

music_folder = music_folder.replace("[", "")
music_folder = music_folder.replace("'", "")
music_folder = music_folder.replace("]", "")

# when the program begins scan the songs folder

# create the user_library dictionary
user_library = dict()

# now assign all the song metadata
# change the folder into the songs folder

os.chdir(music_folder)
# iterate through the folder assigning the approriate metadata
for song in os.listdir():
   # the song title is the key, the value is a list with
    user_library[str(song)] = (Song(get_song_metadata(song)[0], get_song_metadata(song)[1], get_song_metadata(song)[2], get_song_metadata(song)[3], get_song_metadata(song)[4], get_song_metadata(song)[5]))

# show the user the library
print("Current Library")
for key, value in user_library.items():
    print(str(value.get_song_title()) + "-" + str(value.get_song_artist()))
    

'''
# Citated Code
- Title: How to Make Hotkeys in Python
- Author: https://nitratine.net
- Date: January 18, 2018
'''


COMBINATIONS = [
    {keyboard.Key.shift}
]


def execute():

    # begining of original input code
    # open the input to take in a command 
    user_command = input(">")


    # perform the action
    if user_command.startswith("view-info:"):
        current_song = str(re.findall("view-info:(.+)", user_command))

        # remove any uncessary characters from the string
        current_song = current_song.replace("[", "")
        current_song = current_song.replace("'", "")
        current_song = current_song.replace("]", "")
        current_song = current_song + ".mp3"

        # run the function
        view_info(user_library[current_song])

        # exit the program
    elif user_command.startswith("quit"):
        exit()

        # play the song
    elif user_command.startswith("play:"):
        current_song = str(re.findall("play:(.+)", user_command))

        current_song = current_song.replace("[", "")
        current_song = current_song.replace("'", "")
        current_song = current_song.replace("]", "")
        current_song = current_song + ".mp3"

        for key, value in user_library.items():
            if key == current_song:
                playsound(key, False)

    else:
        print("Invalid choice")

    # end of original input code    

current = set()

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()        

'''
End Of Cited Code
'''