class Song:
    # initiliazation function
    def __init__(self, album_title, song_title, song_artist, album_artist, track_number, release_date):

        # if the entered value is empty, meaning that attribute does not exist
        # assign unknown to the variable

        # holds the title of the album the song is from
        if album_title == "[":
            self.album_title = "Unknown"
        else:
            self.album_title = album_title

        # holds the title of the song
        if song_title == "[":
            self.song_title = "Unknown"
        else:
            self.song_title = song_title

        # holds the artist credited on the song
        if song_artist == "[":
            self.song_artist = "Unknown"
        else:
            self.song_artist = song_artist

        # holds the artist credited on the album
        if album_artist == "[":
            self.album_artist = "Unknown"
        else:
            self.album_artist = album_artist

        # holds the track number of the song
        if track_number == "[":
            self.track_number = "Unknown"
        else:
            self.track_number = track_number

        # holds the release date of the song
        if release_date == "[":
            self.release_date = "Unknown"
        else:
            self.release_date = track_number



    # get functions
    def get_album_title(self):
        return self.album_title

    def get_song_title(self):
        return self.song_title

    def get_song_artist(self):
        return self.song_artist

    def get_album_artist(self):
        return self.album_artist

    def get_track_number(self):
        return self.track_number

    def get_release_date(self):
        return self.release_date
