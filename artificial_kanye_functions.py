### artificial_kanye_functions.py
### Team Poznań
### 2020-05-29
### A core functionality module for artificial_kanye


import librosa
import numpy as np
import sounddevice as sd
import os
import random
from scipy.io.wavfile import write as scipy_write

#
def load_file(filename):
    y, sr = librosa.load(filename, sr=None)
    return y, sr

# function for isolation of "the half of a second"
def segmentation(y, sr):
    if len(y) > sr//2:
        segment = y[:sr//2]
        return segment
    else:
        return y

# function to create a segment list
def list_segments(y, sr):
    number_of_segments = len(y)//(sr//2) + 1 # how many segments there should be based on the amt of samples and the sample rate
    segment_list = []
    for i in range(number_of_segments): # add segments to a list
        segment = segmentation(y, sr)
        segment_list.append(segment)
        y = y[sr//2:]
    return segment_list

def pitch_shifted_file(y,sr,pitch):
    segments_original = list_segments(y,sr)
    y_shift = librosa.effects.pitch_shift(segments_original[0], sr, pitch+random.randint(-5,5))
    for segment in segments_original[1:]:
        segment = librosa.effects.pitch_shift(segment, sr, pitch+random.randint(-5,5))
        y_shift += segment
    return y_shift,sr

def playback(y,sr):
    sd.play(y,sr) # play audio
    sd.wait() # wait until done playing

def stop_playback():
    sd.stop()

def record_audio_file(filename, rate, length):
    #recording audio file
    recording = sd.rec(int(length * rate), samplerate=rate, channels=2)
    #waiting until recording is finished
    sd.wait()
    #saving the recorded audio file
    if filename == "(default)":
        write_filename = os.path.join('res','sound', "recording_output.wav")
    else:
        write_filename = os.path.join('res','sound', filename + ".wav")
    scipy_write(write_filename, rate, recording)
