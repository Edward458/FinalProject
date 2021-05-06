# FinalProject
Edward Mesa

# Program Description

This program is a terminal based mp3 player. User must place all the songs in a folder, which can be specified in the config.txt file, that folder will be scanned and a track list will print on screen. From here the user can either view information about the a song in their library, play a song in their library, or quit out of the program. The user can perform any of these tasks by pressing the shift key and typing view-info:song to view the selected songs information, play:song to play the selected song, or quit to exit the program.



# Modules used (and how to download them)
- Mutagen (pip install mutagen)
    - This module was used to extract the metadata from the mp3 file, these include the song title, song artist, album, track number, etc.
- Playsound (pip install playsound)
    - This module was used to play the mp3 file.
- pyinput (pip install pyinput)
    - This module was used to capture user keyboard input.

# Future Work
- Multiple Playlists
    - The playlist feature that was in earlier version of the program did not work well, and I decided it would be better for user experience to have the user choose their own song folder with the config file. Later I would like to allow the user to have multiple lists of songs in the program at once, whether that be by allowing the user to selected multiple song folders, or some data structure inside the program.

- Song Selection
    - In the current iteration of the program, users must close and reopen it in order to play a different song from their library. This is due to the limitations of the playsound module, however this was the only module I could get to work with mp3s reliably. In future version of the program, I hope users would be able to more easily switch songs.

- Song Controls
    - Once again due to the limitations of the playsound module, users are unable to pause, skip, fastfoward or rewind songs. In the future I would like to implement more robust song controls.


# Citated Code
- Title: How to Make Hotkeys in Python
- Author: https://nitratine.net
- Date: January 18, 2018

# Code as it appears in the source

    # The key combination to check
    COMBINATIONS = [
        {keyboard.Key.shift, keyboard.KeyCode(char='a')},
        {keyboard.Key.shift, keyboard.KeyCode(char='A')}
    ]

        # The currently active modifiers
    current = set()

    def execute():
        print ("Do Something")

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

# Code as it appears in project
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
