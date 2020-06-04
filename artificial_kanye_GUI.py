### artificial_kanye_GUI.py
### Team Poznań
### 2020-06-04
### A GUI module for artificial_kanye

from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import os
import shutil
import soundfile as sf
import artificial_kanye_functions as akf
import artificial_kanye_TTS as aktts

#some functions made just to test if the buttons are working properly
def play_audio_file():
    print("Play")

# def pause_audio_file():
#     print("Pause")
# Pausing doesn't work for now

def stop_audio_file():
    akf.stop_playback()

def change_volume(volume):
    print(volume)

def change_pitch(pitch):
    print(pitch)

# copies the file into the resource folder and repopulates the files listbox
def copy_audio_file():
    source_file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("wav files","*.wav"),("ogg files","*.ogg")))
    directory = os.path.join('res', 'sound')
    shutil.copy(source_file, directory)
    audio_files_listbox.delete(0, END)
    soundfiles_directory = os.path.join('res','sound')
    soundfiles_all = os.listdir(soundfiles_directory)
    soundfiles = [filename for filename in soundfiles_all if re.search(r'.+(\.wav$|\.ogg$)', filename)]
    for soundfile in soundfiles:
        audio_files_listbox.insert(END, soundfile)

# creates a new window with TTS functions
def open_tts_dialog():
    tts_window = Toplevel(program_window)
    tts_window.title("Text-to-speech")
    icon_filename = os.path.join('res','img','kanye_license_icon.ico')
    tts_window.iconbitmap(icon_filename)
    text_entry_label = Label(tts_window, text="Type in text to write to file:")
    text_entry = Entry(tts_window)
    filename_entry_label = Label(tts_window, text="Choose filename (can leave default):")
    filename_entry = Entry(tts_window)
    filename_entry.insert(END, "(default)")
    save_button = Button(tts_window, text="Save", command = lambda:save_tts_file(text_entry.get(), filename_entry.get()))
    text_entry_label.grid(row = 0, column = 0, sticky=W)
    text_entry.grid(row = 0, column = 1)
    filename_entry_label.grid(row = 1, column = 0, sticky=W)
    filename_entry.grid(row = 1, column = 1)
    save_button.grid(row = 2, column = 0, columnspan=2, sticky=W+E+N+S, padx=2, pady=2)


def save_tts_file(text, filename):
    if filename == "(default)":
        aktts.kanye_text_to_speech(text, "text_to_speech_output")
    else:
        aktts.kanye_text_to_speech(text, filename)
    audio_files_listbox.delete(0, END)
    soundfiles_directory = os.path.join('res','sound')
    soundfiles_all = os.listdir(soundfiles_directory)
    soundfiles = [filename for filename in soundfiles_all if re.search(r'.+(\.wav$|\.ogg$)', filename)]
    for soundfile in soundfiles:
        audio_files_listbox.insert(END, soundfile)


def record_voice():
    record_window = Toplevel(program_window)
    record_window.title("Record audio")
    icon_filename = os.path.join('res','img','kanye_license_icon.ico')
    record_window.iconbitmap(icon_filename)
    record_filename_label = Label(record_window, text = "Filename (can leave default):")
    record_filename = Entry(record_window)
    record_filename.insert(END, "(default)")
    record_samplerate_label = Label(record_window, text="Sampling rate:")
    record_samplerate = Entry(record_window)
    record_samplerate.insert(END, "44100")
    record_length_label = Label(record_window, text="Length (seconds):")
    record_length = Entry(record_window)
    record_length.insert(END, "10")
    save_button = Button(record_window, text="Record", command=lambda:akf.record_audio_file(record_filename.get(), int(record_samplerate.get()), int(record_length.get())))
    record_filename_label.grid(row=0, column=0, sticky=W)
    record_filename.grid(row=0, column=1)
    record_samplerate_label.grid(row=1, column=0, sticky=W)
    record_samplerate.grid(row=1,column=1)
    record_length_label.grid(row=2,column=0, sticky=W)
    record_length.grid(row=2,column=1)
    save_button.grid(row=3, column=0, columnspan = 2, sticky=W+E+N+S, padx=2, pady=2)

def apply_pitch_shift():
    src_file = os.path.join('res','sound',audio_files_listbox.get(audio_files_listbox.curselection()))
    y, sr = akf.load_file(src_file)
    y_shift, sr = akf.pitch_shifted_file(y,sr,int(pitch_control_slider.get()))
    output_file_dir = os.path.join('res', 'output', 'output.wav')
    sf.write(output_file_dir, y_shift, sr, subtype='PCM_24')


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
playback_buttons = Frame(program_window)
playback_buttons.pack(side = BOTTOM)

#constructing a frame for upload and text-to-speech buttons
file_buttons = Frame(program_window)
file_buttons.place(relx=0.5, rely=0.88, anchor=CENTER)

#constructing a frame pitch, volume sliders
sliders = Frame(program_window)
sliders.place(relx=0.8, rely=0.67, anchor=CENTER)

#making a play button
play_image_filename = os.path.join('res','img','play.png')
play_image = PhotoImage(file = play_image_filename)
play_button = Button(playback_buttons, image = play_image, command = play_audio_file)
play_button.pack(side = LEFT)

# making a pause button
# pause_image_filename = os.path.join('res','img','pause.png')
# pause_image = PhotoImage(file = pause_image_filename)
# pause_button = Button(playback_buttons, image = pause_image, command = pause_audio_file)
# pause_button.pack(side = LEFT)
# Pausing doesn't work for now

#making a stop button
stop_image_filename = os.path.join('res','img','stop.png')
stop_image = PhotoImage(file = stop_image_filename)
stop_button = Button(playback_buttons, image = stop_image, command = stop_audio_file)
stop_button.pack(side = LEFT)

#making a button for voice recording
mic_image_filename = os.path.join('res','img','microphone.png')
mic_image = PhotoImage(file = mic_image_filename)
voice_recording_button = Button(playback_buttons, image = mic_image, command = record_voice)
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
file_loading_button = Button(file_buttons, text = "Upload an audio file from your computer", command = copy_audio_file)
file_loading_button.pack(side = TOP)

file_loading_button = Button(file_buttons, text = "Text-to-speech", command = open_tts_dialog)
file_loading_button.pack(side = TOP)

#making a listbox frame
listbox_frame = Frame(program_window)
listbox_frame.place(relx=0.3, rely=0.67, anchor=CENTER)

#making a scrollbar for the listbox
scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)

#making a listbox of audio files and applying a scrollbar to it
audio_files_listbox = Listbox(listbox_frame, yscrollcommand=scrollbar.set)
audio_files_listbox.pack(side = LEFT)
scrollbar.config(command=audio_files_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

#inserting audio files from the resource folder to the listbox
soundfiles_directory = os.path.join('res','sound')
soundfiles_all = os.listdir(soundfiles_directory)
soundfiles = [filename for filename in soundfiles_all if re.search(r'.+(\.wav$|\.ogg$)', filename)]
for soundfile in soundfiles:
    audio_files_listbox.insert(END, soundfile)

#making a listbox for melodies
melody_listbox = Listbox(listbox_frame)
melody_listbox.pack(side=RIGHT)

#insert option to randomize "melody"
melody_listbox.insert(END, "Random")

#button to apply pitch shift
ps_button = Button(sliders, text= "Apply", command=apply_pitch_shift)
ps_button.pack(side=BOTTOM)

#closing the program when closing the window
program_window.protocol("WM_DELETE_WINDOW", close_the_window)

#putting everithing in a mainloop
def start_GUI():
    program_window.mainloop()

start_GUI()
