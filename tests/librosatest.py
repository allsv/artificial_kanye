import librosa
import numpy as np
import sounddevice as sd
import soundfile as sf


# get the example audio file
filename = "../res/example.wav"

# Load the audio as a waveform `y`
# Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# get the duration of the input file
input_duration = librosa.get_duration(y, sr)

#
y_shift = librosa.effects.pitch_shift(y, sr, 4)

#
shifted_duration = librosa.get_duration(y_shift, sr)

#
y_stretch = librosa.effects.time_stretch(y, shifted_duration/input_duration)

#
stretched_duration = librosa.get_duration(y_stretch, sr)

print(input_duration)
print(shifted_duration)
print(stretched_duration)

# write file
sf.write('test_output_file.wav', y_shift, sr, subtype='PCM_24')
