import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

# Load audio file
sample_rate, audio = wavfile.read("traffic_audio.wav")

# Convert to mono if needed
if len(audio.shape) > 1:
    audio = audio[:,0]

# Compute spectrogram
frequencies, times, Sxx = spectrogram(audio, sample_rate)

# Plot spectrogram
plt.pcolormesh(times, frequencies, Sxx)
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (s)")
plt.title("Traffic Acoustic Spectrogram")
plt.show()
