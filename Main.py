import pygame
import os
from tkinter import filedialog
from tkinter import *

# Initialize pygame
pygame.init()

# Create a GUI for your music player
root = Tk()
root.title("Music Player")

# Create a listbox to display the playlist
playlist = Listbox(root, bg="black", fg="white", selectbackground="green")
playlist.pack(fill="both", expand="yes")

# Create buttons for controls
play_button = Button(root, text="Play")
stop_button = Button(root, text="Stop")
pause_button = Button(root, text="Pause")
resume_button = Button(root, text="Resume")
add_button = Button(root, text="Add Song")

play_button.pack()
stop_button.pack()
pause_button.pack()
resume_button.pack()
add_button.pack()

# Define functions for the music player controls
def play_music():
    current_song = playlist.get(playlist.curselection())
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def add_song():
    file_path = filedialog.askopenfilename()
    playlist.insert(END, file_path)

# Bind the control functions to the buttons
play_button.config(command=play_music)
stop_button.config(command=stop_music)
pause_button.config(command=pause_music)
resume_button.config(command=resume_music)
add_button.config(command=add_song)

# Start the main loop
root.mainloop()
