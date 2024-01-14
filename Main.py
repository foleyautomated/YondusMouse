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
import time

HZ_FLOOR = 0; 
HZ_CEILNG = 2000;
VOL_THRESHOLD = 400;
PXLS_PER_NUDGE = 50;
VOL_CLICK_MIN = 2000;


def rangeToDegrees(floor, ceiling, value):
    rng = ceiling - floor;
    return round((value/rng) * 360)

def nudge(hypotenuse, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    x_nudge = round(hypotenuse * math.cos(angle_radians))
    y_nudge = round(hypotenuse * math.sin(angle_radians))
    x_coord, y_coord = pyautogui.position()
    pyautogui.moveTo(x_coord + x_nudge, y_coord + y_nudge, duration =0.1)

def calculate_volume(audio_data):
    rms = np.sqrt(np.mean(np.square(audio_data)))
    return rms

def max_volume(audio_data):
    rms = np.sqrt(np.mean(np.max(audio_data)))
    return rms


while(1) :
    #Bullshit I dont understand
    sample_rate = 44100  # 44.1 kHz is a common sample rate
    duration = 1
    audio_input = sd.rec(int(sample_rate * duration), channels=1, dtype='int16')
    sd.wait()
    audio_input_float = audio_input.flatten().astype(np.float32)
    fft_result = np.fft.fft(audio_input_float)
    fft_freq = np.fft.fftfreq(len(fft_result), d=1/sample_rate)
    peak_freq_index = np.argmax(np.abs(fft_result))

    #Volume
    volume = round(calculate_volume(audio_input_float))

    #Actual Code
    peak_frequency = round(np.abs(fft_freq[peak_freq_index])) 

    degrees = rangeToDegrees(HZ_FLOOR, HZ_CEILNG, peak_frequency)
    print(f"[{time.time()}] Degrees: {degrees} Frequency: {peak_frequency}Hz Volume: {volume}")
    if(volume > VOL_CLICK_MIN) :
        print(f"CLICKING! Volume: {volume}")
        pyautogui.click(0.5)
        
    elif(volume > VOL_THRESHOLD and volume < VOL_CLICK_MIN) :
        nudge(PXLS_PER_NUDGE, degrees)



