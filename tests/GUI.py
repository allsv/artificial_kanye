from tkinter import *

#some functions made just to test if the buttons are working properly
def play_audio_file():
    print("Play")

def pause_audio_file():
    print("Pause")

def stop_audio_file():
    print("Stop")

def change_volume(volume):
    print (volume)

def change_pitch(pitch):
    print(pitch)

def load_an_audio_file():
    print("Audio file load")

def record_voice():
    print("Voice recording")

#making the window of our program
program_window = Tk()

#setting the window's name
program_window.title("Artificial Kanye")

#setting the window's size
program_window.geometry("500x600")

#setting the window's icon
program_window.iconbitmap('kanye_icon.ico')

#displaing some greeting at the top of the window
greeting = Label(program_window, text = "Witaj w Artificial Kanye!")
greeting.pack()

#displaying Kanye's face in the center of the window
kanye_face = PhotoImage(file = 'kanye_sad.png')
kanye_face_label = Label(program_window, image = kanye_face)
kanye_face_label.pack()

#constructing a frame for play, pause, stop buttons
buttons = Frame(program_window)
buttons.pack(side = BOTTOM)

#constructing a frame pitch, volume sliders
sliders = Frame(program_window)
sliders.pack()

#making a play button
play_image = PhotoImage(file = 'play.png')
play_button = Button(buttons, image = play_image, command = play_audio_file)
play_button.pack(side = LEFT)

#making a pause button
pause_image = PhotoImage(file = 'pause.png')
pause_button = Button(buttons, image = pause_image, command = pause_audio_file)
pause_button.pack(side = LEFT)

#making a stop button
stop_image = PhotoImage(file = 'stop.png')
stop_button = Button(buttons, image = stop_image, command = stop_audio_file)
stop_button.pack(side = LEFT)

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
file_loading_button.pack(side = LEFT)

#making a button for voice recording
microphone_image = PhotoImage(file = 'microphone.png')
voice_recording_button = Button(program_window, image = microphone_image, command = record_voice)
voice_recording_button.pack(side = RIGHT)

#putting everithing in a mainloop
program_window.mainloop()
