import mutagen
import re
import os
from Playlist import *

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

def print_menu():
    print("Show library (sl)")
    print("Show playlists (sp)")
    print("Edit playlists (ep)")
    print("Remove playlists (rp)")
    print("Remove Song (rs)")
    print("Scan Folder (sf)")
    print("Quit (q)")

def view_info(current_song):
    # print all the metadata of the song
    print("Title: " + str(current_song.get_song_title()))
    print("Artist: " + str(current_song.get_song_artist()))
    print("Album: " + str(current_song.get_album_title()) + " by " + str(current_song.get_album_artist()))
    print("Track Number: " + str(current_song.get_track_number()))
   # print("Release Date: " + str(current_song.get_release_date()))