import mutagen
import re
from Song import Song
from Playlist import Playlist
from functions import *
from pygame import *
import os

print("Random terminal based mp3 player (Name subject to change)")



print_menu()



user_library = Playlist()
user_playlist = list()

while True:
    userChoice = input("")

    # statement for the varius choices
    if userChoice == "sl":
        user_library.get_song_list()
    elif userChoice == "sp":
        for playlist in user_playlist:
            print(playlist.get_playlist_name() + " - " + playlist.get_song_number())
    elif userChoice == "ep":
        while True:
            print("Choose the playlist to edit")

            userChoice = input()

            # this will allow the user to create a new playlist
            if userChoice not in user_playlist:
                print("Playlist not found")
                userChoice = input("Would you like to create it\n")

                if userChoice == "yes" || userChoice == "Yes":
                    user_playlist.append(Playlist())
                else:
                    break

            # if the playlist is found
            print("Add song (as)")
            print("Remove song (rs)")
            print("Change name (cn)")

            userChoice = input()

    elif userChoice == "rp":
        print("Choose playlist to remove")
        playlist_to_remove = input("")

        user_playlist.remove(playlist_to_remove)

    elif userChoice == "rs":
        pass
    elif userChoice == "sf":
        try:
            os.chdir("songs")

            # iterate through the folder
            for song in os.listdir():
                # if it is an mp3 file
                if song.endswith(".mp3"):
                    user_library.add_song(Song(get_song_metadata(song)[0], get_song_metadata(song)[1], get_song_metadata(song)[2], get_song_metadata(song)[3], get_song_metadata(song)[4], get_song_metadata(song)[5]))
        except:
            print("Unaviable to open folder")
            print("Please restart program")
    elif userChoice == "q":
        break
    else:
        print("Invalid Input")
