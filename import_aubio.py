import aubio
import numpy as np

# Set up the parameters
samplerate = 44100
win_s = 1024  # window size
hop_s = 512   # hop size

# Create the pitch detector
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)

# Open an audio input stream (replace 'your_microphone_device' with your actual microphone device)
pyaudio = aubio.pyaudio()
stream = pyaudio.open(format=pyaudio.paFloat32,
                      channels=1,
                      rate=samplerate,
                      input=True,
                      frames_per_buffer=hop_s)

# Infinite loop to continuously capture and print the detected pitch
while True:
    samples, read = stream.read(hop_s)
    pitch = pitch_o(samples)[0]
    
    # Convert MIDI note to frequency
    frequency = aubio.midi2freq(pitch)
    
    print(f"Detected MIDI Note: {pitch}, Frequency: {frequency} Hz")