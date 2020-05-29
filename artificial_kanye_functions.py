### artificial_kanye_functions.py
### Team Poznań
### 2020-05-29
### A core functionality module for artificial_kanye


import librosa
import numpy as np
import sounddevice as sd



def estimate_tuning(file):
    y, sr = librosa.load(file)
    return librosa.piptrack(y, sr)


# def
