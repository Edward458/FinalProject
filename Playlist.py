from Song import Song

# the playlist object
class Playlist:
    def __init__(self):
        # set the default values for playlist name and songs list
        self.playlist_name = "New playlist " + str(4) # replace 4 with a random number
        self.song_list = list() # blank list for the song list


    def set_playlist_name(self, playlist_name):
        # set the name of the playlist
        self.playlist_name = playlist_name


    def add_song(self, song_name):
        # add the song the playlist
        self.song_list.append(song_name)


    def get_playlist_name(self):
        return self.playlist_name

    def get_song_list(self):
        for song in self.song_list:
            print("-" + song.get_song_title() + " - " + song.get_song_artist())
