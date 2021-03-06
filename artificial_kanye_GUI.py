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
import VolumeControl

#some functions made just to test if the buttons are working properly
# plays the audio file
def play_audio_file():
    if not pitch_shifting_applied: #pitch not applied
        src_file = os.path.join('res','sound',audio_files_listbox.get(audio_files_listbox.curselection()))
        y_src, sr_src = akf.load_file(src_file)
        akf.playback(y_src, sr_src)
    else: #with pitch applied
        src_file = os.path.join('res','output','output.wav')
        y_src_pitch, sr_src_pitch = akf.load_file(src_file)
        akf.playback(y_src_pitch, sr_src_pitch)

# def pause_audio_file():
#     print("Pause")
# Pausing doesn't work for now

# stopping playing the audio file
def stop_audio_file():
    akf.stop_playback()

# volume control
def change_volume(volume):
    audio_controller = VolumeControl.AudioController('python.exe')
    volume_value = float(volume) * 0.1
    audio_controller.set_volume(volume_value)

# pitch control
def change_pitch(pitch):
    print("Pitch:", str(pitch))

# copies the file into the resource folder and repopulates the files listbox
def copy_audio_file():
    source_file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("wav files","*.wav"),("ogg files","*.ogg")))
    directory = os.path.join('res', 'sound')
    shutil.copy(source_file, directory)
    #repopulate file listbox
    audio_files_listbox.delete(0, END)
    print("Repopulating file listbox")
    soundfiles_directory = os.path.join('res','sound')
    soundfiles_all = os.listdir(soundfiles_directory)
    soundfiles = [filename for filename in soundfiles_all if re.search(r'.+(\.wav$|\.ogg$)', filename)]
    for soundfile in soundfiles:
        audio_files_listbox.insert(END, soundfile)
        print(soundfile,"added to file listbox")

def save_audio_file():
    directory = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("wav files","*.wav"),("ogg files","*.ogg")))
    outfile = os.path.join('res','output','output.wav')
    shutil.move(outfile, directory)

# creates a new window with TTS dialogue
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
    # making save button
    save_button = Button(tts_window, text="Save", command = lambda:save_tts_file(text_entry.get(), filename_entry.get()))
    text_entry_label.grid(row = 0, column = 0, sticky=W)
    text_entry.grid(row = 0, column = 1)
    filename_entry_label.grid(row = 1, column = 0, sticky=W)
    filename_entry.grid(row = 1, column = 1)
    save_button.grid(row = 2, column = 0, columnspan=2, sticky=W+E+N+S, padx=2, pady=2)

# saving TTS file
def save_tts_file(text, filename):
    if filename == "(default)":
        aktts.kanye_text_to_speech(text, "text_to_speech_output")
    else:
        aktts.kanye_text_to_speech(text, filename)
    #repopulate file listbox
    audio_files_listbox.delete(0, END)
    print("Repopulating file listbox")
    soundfiles_directory = os.path.join('res','sound')
    soundfiles_all = os.listdir(soundfiles_directory)
    soundfiles = [filename for filename in soundfiles_all if re.search(r'.+(\.wav$|\.ogg$)', filename)]
    for soundfile in soundfiles:
        audio_files_listbox.insert(END, soundfile)
        print(soundfile,"added to file listbox")

#letting the user record their own audio file
def record_voice():
    #buttons making up the interface that allows the user recording of the audiofile
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

#applying chosen pitch on the original audio
def apply_pitch_shift():
    #joining pitch button with the shifting pitch function
    global pitch_shifting_applied
    src_file = os.path.join('res','sound',audio_files_listbox.get(audio_files_listbox.curselection()))
    y, sr = akf.load_file(src_file)
    y_shift, sr_shift = akf.pitch_shifted_file(y,sr,int(pitch_control_slider.get()))
    print("apply_pitch_shift - y_shift:",y_shift)
    print("apply_pitch_shift - sr_shift:",sr_shift)
    output_file_dir = os.path.join('res', 'output', 'output.wav')
    sf.write(output_file_dir, y_shift, sr_shift, subtype='PCM_24')
    pitch_shifting_applied = True


def close_the_window():
    stop_audio_file()
    program_window.destroy()

#resetting audio file to its original shape (without the change in the pitch)
def reset_file():
    global pitch_shifting_applied
    pitch_shifting_applied = False


#making the window of our program
program_window = Tk()

# variable to test if pitch shifting has been done
pitch_shifting_applied = False

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
play_button.pack(side = LEFT)#postitioning the play button

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

#making a save file button
save_image_filename = os.path.join('res','img','save.png')
save_image = PhotoImage(file = save_image_filename)
save_button = Button(playback_buttons, image = save_image, command = save_audio_file)
save_button.pack(side = LEFT)

#making a button for voice recording
mic_image_filename = os.path.join('res','img','microphone.png')
mic_image = PhotoImage(file = mic_image_filename)
voice_recording_button = Button(playback_buttons, image = mic_image, command = record_voice)
voice_recording_button.pack(side = RIGHT)

#making a volume control slider
volume_control_slider = Scale(sliders, from_=10, to = 0, command = change_volume, label = "Volume")
volume_control_slider.set(5)
volume_control_slider.grid(row=0, column=0)

#making a pitch control slider
pitch_control_slider = Scale(sliders, from_= 10, to = -10, command = change_pitch, label = "Pitch")
pitch_control_slider.set(0)#starting position of the slider
pitch_control_slider.grid(row=0, column=1)#positioning the slader

#making an audio file loading button
file_loading_button = Button(file_buttons, text = "Import an audio file from your computer", command = copy_audio_file)
file_loading_button.pack(side = TOP)

file_loading_button = Button(file_buttons, text = "Text-to-speech", command = open_tts_dialog)
file_loading_button.pack(side = TOP)

#making a listbox frame
listbox_frame = Frame(program_window)
listbox_frame.place(relx=0.2, rely=0.67, anchor=CENTER)#postioning the listbox frame

#making a scrollbar for the listbox
scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)

#making a listbox of audio files and applying a scrollbar to it
audio_files_listbox = Listbox(listbox_frame, yscrollcommand=scrollbar.set)
audio_files_listbox.pack(side = LEFT)
scrollbar.config(command=audio_files_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
audio_files_listbox.bind('<<ListboxSelect>>', reset_file)

#inserting audio files from the resource folder to the listbox
soundfiles_directory = os.path.join('res','sound')
soundfiles_all = os.listdir(soundfiles_directory)
soundfiles = [filename for filename in soundfiles_all if re.search(r'.+(\.wav$|\.ogg$)', filename)]
for soundfile in soundfiles:
    audio_files_listbox.insert(END, soundfile)

#making a listbox for melodies
# melody_listbox = Listbox(listbox_frame)
# melody_listbox.pack(side=RIGHT)

#insert option to randomize "melody"
# melody_listbox.insert(END, "Random")

#button to apply pitch shift
ps_button = Button(sliders, text= "Apply", command=apply_pitch_shift)
ps_button.grid(row=1, column=0, columnspan=2, sticky=W+N+S, padx=17) #positioning the button
ps_button.config(width = 15 )

#closing the program when closing the window
program_window.protocol("WM_DELETE_WINDOW", close_the_window)

#putting everithing in a mainloop
def start_GUI():
    program_window.mainloop()

start_GUI()
