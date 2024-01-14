import sounddevice as sd
import numpy as np
import math
import pyautogui
import pyaudio
import wave
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import statistics
import pyautogui

while(1) :
    # Set the sample rate and duration
    sample_rate = 44100  # 44.1 kHz is a common sample rate
    duration = 1  # seconds

    # Capture audio from the microphone
    audio_input = sd.rec(int(sample_rate * duration), channels=1, dtype='int16')
    sd.wait()

    # Convert the input to floating-point values
    audio_input_float = audio_input.flatten().astype(np.float32)

    # Perform Fast Fourier Transform (FFT) to get the frequency spectrum
    fft_result = np.fft.fft(audio_input_float)
    fft_freq = np.fft.fftfreq(len(fft_result), d=1/sample_rate)

    # Find the peak frequency
    peak_freq_index = np.argmax(np.abs(fft_result))
    peak_frequency = np.abs(fft_freq[peak_freq_index])

    print(f"Peak Frequency: {peak_frequency} Hz")

    while(1) :
        sample_rate = 44100  # 44.1 kHz is a common sample rate
        duration = 1
        audio_input = sd.rec(int(sample_rate * duration), channels=1, dtype='int16')
        sd.wait()
        audio_input_float = audio_input.flatten().astype(np.float32)
        fft_result = np.fft.fft(audio_input_float)
        fft_freq = np.fft.fftfreq(len(fft_result), d=1/sample_rate)
        peak_freq_index = np.argmax(np.abs(fft_result))
        peak_frequency = np.abs(fft_freq[peak_freq_index])
        print(f"Peak Frequency: {peak_frequency} Hz")