from tkinter import *
from PIL import Image
from PIL import ImageTk
import os.path

#some functions made just to test if the buttons are working properly
def play_audio_file():
    print("Play")

def pause_audio_file():
    print("Pause")

def stop_audio_file():
    print("Stop")

def change_volume(volume):
    print(volume)

def change_pitch(pitch):
    print(pitch)

def load_an_audio_file():
    print("Audio file load")

def record_voice():
    print("Voice recording")

def close_the_window():
    stop_audio_file()
    program_window.destroy()


#making the window of our program
program_window = Tk()

#setting the window's name
program_window.title("Artificial Kanye")

#changing the background to orange
#program_window.configure(background = 'orange')

#setting the window's size
program_window.geometry("500x560")

#setting the window's icon
icon_filename = os.path.join('res','img','kanye_license_icon.ico')
program_window.iconbitmap(icon_filename)

#displaing some greeting at the top of the window
greeting = Label(program_window, text = "Welcome to Artificial Kanye!")
greeting.pack()

#displaying Kanye's face in the center of the window
kanye_face_width = 220
kanye_face_height = 254
kanye_img_file_directory = os.path.join('res','img','kanye_license.png')
kanye_img_file = Image.open(kanye_img_file_directory)
kanye_img_file = kanye_img_file.resize((kanye_face_width,kanye_face_height), Image.ANTIALIAS)
kanye_face = ImageTk.PhotoImage(kanye_img_file)
kanye_face_label = Label(program_window, image = kanye_face)
kanye_face_label.pack()

#constructing a frame for play, pause, stop buttons
buttons = Frame(program_window)
buttons.pack(side = BOTTOM)

#constructing a frame pitch, volume sliders
sliders = Frame(program_window)
sliders.place(relx=0.7, rely=0.67, anchor=CENTER)

#making a play button
play_image_filename = os.path.join('res','img','play.png')
play_image = PhotoImage(file = play_image_filename)
play_button = Button(buttons, image = play_image, command = play_audio_file)
play_button.pack(side = LEFT)

#making a pause button
pause_image_filename = os.path.join('res','img','pause.png')
pause_image = PhotoImage(file = pause_image_filename)
pause_button = Button(buttons, image = pause_image, command = pause_audio_file)
pause_button.pack(side = LEFT)

#making a stop button
stop_image_filename = os.path.join('res','img','stop.png')
stop_image = PhotoImage(file = stop_image_filename)
stop_button = Button(buttons, image = stop_image, command = stop_audio_file)
stop_button.pack(side = LEFT)

#making a button for voice recording
mic_image_filename = os.path.join('res','img','microphone.png')
mic_image = PhotoImage(file = mic_image_filename)
voice_recording_button = Button(buttons, image = mic_image, command = record_voice)
voice_recording_button.pack(side = RIGHT)

#making a volume control slider
volume_control_slider = Scale(sliders, from_=10, to = 1, command = change_volume, label = "Volume")
volume_control_slider.set(5)
volume_control_slider.pack(side = LEFT)

#making a pitch control slider
pitch_control_slider = Scale(sliders, from_= 10, to = 1, command = change_pitch, label = "Pitch")
pitch_control_slider.set(5)
pitch_control_slider.pack(side = LEFT)

#making an audio file loading button
file_loading_button = Button(program_window, text = "Upload an audio file from your computer", command = load_an_audio_file)
file_loading_button.place(relx=0.5, rely=0.905, anchor=CENTER)

#making a listbox frame
listbox_frame = Frame(program_window)
listbox_frame.place(relx=0.2, rely=0.67, anchor=CENTER)

#making a scrollbar for the listbox
scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)

#making a listbox of audio files and applying a scrollbar to it
audio_files_listbox = Listbox(listbox_frame, yscrollcommand=scrollbar.set)
audio_files_listbox.pack(side = LEFT)
scrollbar.config(command=audio_files_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

#inserting an audio file name in a listbox
audio_files_listbox.insert(END, 'example.wav')

#closing the program when closing the window
program_window.protocol("WM_DELETE_WINDOW", close_the_window)

#putting everithing in a mainloop
def start_GUI():
    program_window.mainloop()

start_GUI()
