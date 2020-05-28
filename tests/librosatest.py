### artificial_kanye/tests/librosatest.py
### Paweł Szczepański (Team Poznań)
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
y, sr = librosa.load(filename)

# play loaded audio file
sd.play(y,sr)
# Wait until the file is done playing
status = sd.wait()

# pitch shift the input waveform by 4 semitones
y_shift = librosa.effects.pitch_shift(y, sr, 4)

# play pitch shifted audio file
sd.play(y_shift, sr)
# Wait until the file is done playing
status = sd.wait()

# write the pitch shifted waveform to file
sf.write('test_output_file.wav', y_shift, sr, subtype='PCM_24')
