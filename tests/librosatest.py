### artificial_kanye/tests/librosatest.py
### Team Poznań
### 2020-05-27
### This module is made to test the functionality of the pitch_shift function from librosa.


import librosa
import numpy as np
import sounddevice as sd
import soundfile as sf


# get the example audio file
filename = "../res/example.wav"

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
