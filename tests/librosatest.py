### artificial_kanye/tests/librosatest.py
### Team Poznań
### 2020-05-27
### This module is made to test the functionality of the pitch_shift function from librosa.


import librosa
import numpy as np
import sounddevice as sd
import soundfile as sf


# get the example audio file
filename = "../res/sound/example.wav"

# Load the audio as a waveform `y`
# Store the sampling rate as `sr`
y, sr = librosa.load(filename, sr=None)

# checking the type and sampling rate (just a test)
print(type(y))
print(sr)

## we could use window functions (librosa.filters.getwindow(hann, sr//2) ?)

# the following code needs to be converted into a loop and wrapped into a function
# if we figure out window functions, we use that instead, but the general rule is the same

# the first and second "half-second" of a file (calculated based on sampling rate)
def segmentation(y, sr):
# function for isolation of "the half of a second"
    if len(y) > sr//2:
        segment = y[:sr//2]
        return segment
    else:
        return y
#place for another function to create a list adding elements created in the last function and looping them
#aforementioned function, although not working as it should at the moment:
#def list_segments(filename):
   # y, sr = librosa.load(filename, sr=None)
   #segment_list = []
   # segment_list.append(segmentation(y,sr))
    #return segment_list

def list_segments(y, sr):
    number_of_segments = len(y)//(sr//2) + 1
    segment_list = []
    for i in range(number_of_segments):
        segment = segmentation(y, sr)
        segment_list.append(segment)
        y = y[sr//2:]
    return segment_list

print(list_segments(y,sr))


# the first and second "half-second" of a file (calculated based on sampling rate)
first_half_second = y[:sr//2]
second_half_second = y[sr//2:sr]

# play the combination of the above snippets
sd.play(first_half_second+second_half_second,sr)
# Wait until the audio is done playing
status = sd.wait()

# pitch shift the waveform by 4 semitones
y_shift1 = librosa.effects.pitch_shift(first_half_second, sr, 4)
y_shift2 = librosa.effects.pitch_shift(second_half_second, sr, -4)

# play pitch shifted audio
sd.play(y_shift1+y_shift2, sr)
# Wait until the audio is done playing
status = sd.wait()

# write the pitch shifted waveform to file
sf.write('test_output_file.wav', y_shift1+y_shift2, sr, subtype='PCM_24')
