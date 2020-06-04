import sounddevice as sd
from scipy.io.wavfile import write

#setting the recording sampling rate
recording_rate = 44100

#setting the recording length
recording_length = 5

#recording basic 5 second audio file
recording = sd.rec(int(recording_length * recording_rate), samplerate=recording_rate, channels=2)

#waiting until recording is finished
sd.wait()

#saving the recorded audio file
write('recording_output.wav', recording_rate, recording)

