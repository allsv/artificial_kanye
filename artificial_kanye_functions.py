### artificial_kanye_functions.py
### Team Poznań
### 2020-05-29
### A core functionality module for artificial_kanye


import librosa
import numpy as np
import sounddevice as sd


# function for isolation of "the half of a second"
def segmentation(y, sr):
    if len(y) > sr//2:
        segment = y[:sr//2]
        return segment
    else:
        return y
