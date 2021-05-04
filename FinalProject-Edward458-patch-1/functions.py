import mutagen
import re
import os
from Playlist import *

def get_song(music_folder):
    songs_list = list()
    # first enter the input folder
    os.chdir(music_folder)

    # iterate through the folder
    for song in os.listdir():
        # if it is an mp3 file
        if song.endswith(".mp3"):
            # add it to the song_list list
            songs_list.append(song)

    # return the list
    return songs_list


# get song metadata
def get_song_metadata(current_song):

    song_metadata = str(mutagen.File(str(current_song), easy=True))

    # Variables to get song metadata
    album_title = re.findall("'album':\s\['(.+?)'\]", song_metadata)
    song_title = re.findall("'title':\s\['(.+?)'\]", song_metadata)
    song_artist = re.findall("'artist':\s\['(.+?)'\]", song_metadata)
    album_artist = re.findall("'albumartist':\s\['(.+?)'\]", song_metadata)
    track_number = re.findall("'tracknumber':\s\['(.+?)'\]", song_metadata)
    release_date = re.findall("'date':\s\['(.+?)'\]", song_metadata)

    # create a list to return all the metadata
    metadata_list = [album_title[0], song_title[0], song_artist[0], album_artist[0], track_number[0], release_date[0]]

    # index 0 holds the album_title
    # index 1 holds the song_title
    # index 2 holds the song_artist
    # index 3 holds album_artist
    # index 4 holds track_number
    # index 5 release_date

    return metadata_list


# create a playlist
def create_playlist():

    the_playlist = Playlist()

    # first ask the user to enter a name for the playlist
    playlist_name = input("Enter a playlist name: ")

    # if the user does not enter a name keep the default playlist name
    # other wise assing the playlist name to the one choosen by the user
    if playlist_name != "":
        the_playlist.set_playlist_name(the_playlist)


    # return the playlist to main
    return the_playlist

def print_menu():
    print("Show library (sl)")
    print("Show playlists (sp)")
    print("Edit playlists (ep)")
    print("Remove playlists (rp)")
    print("Remove Song (rs)")
    print("Scan Folder (sf)")
    print("Quit (q)")
