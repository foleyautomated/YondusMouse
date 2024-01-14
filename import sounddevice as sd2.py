import sounddevice as sd
import numpy as np
import math
import pyautogui

HZ_FLOOR = 20  # Adjust as needed
HZ_CEILING = 20000  # Adjust as needed

def rangeToDegrees(floor, ceiling, value):
    return round((360 * (value - floor)) / (ceiling - floor))

def calculate_volume(audio_data):
    rms = np.sqrt(np.mean(np.square(audio_data)))
    return rms

def nudge(hypotenuse, angle_degrees, volume):
    angle_radians = math.radians(angle_degrees)
    x_nudge = round(hypotenuse * math.cos(angle_radians))
    y_nudge = round(hypotenuse * math.sin(angle_radians))
    x_coord, y_coord = pyautogui.position()
    pyautogui.moveTo(x_coord + x_nudge, y_coord + y_nudge, duration=0.1)
    print(f"Volume: {volume}")

while True:
    # Capture audio from the microphone
    sample_rate = 44100  # 44.1 kHz is a common sample rate
    duration = 0.5
    audio_input = sd.rec(int(sample_rate * duration), channels=1, dtype='int16')
    sd.wait()
    audio_input_float = audio_input.flatten().astype(np.float32)

    # Calculate the volume of the audio
    volume = calculate_volume(audio_input_float)

    # Perform Fast Fourier Transform (FFT) to get the frequency spectrum
    fft_result = np.fft.fft(audio_input_float)
    fft_freq = np.fft.fftfreq(len(fft_result), d=1/sample_rate)
    peak_freq_index = np.argmax(np.abs(fft_result))

    # Get the peak frequency
    peak_frequency = np.abs(fft_freq[peak_freq_index])

    # Convert frequency to degrees
    degrees = rangeToDegrees(HZ_FLOOR, HZ_CEILING, peak_frequency)

    print(f"Degrees: {degrees} Frequency: {peak_frequency} Volume: {volume}")
    
    # Perform the nudge with volume information
    nudge(20, degrees, volume)