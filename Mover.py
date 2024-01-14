#pip3 install pyautogui

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

def nudge(hypotenuse, angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate the length and width
    x_nudge = round(hypotenuse * math.cos(angle_radians))
    y_nudge = round(hypotenuse * math.sin(angle_radians))
    
    x_coord, y_coord = pyautogui.position()
    pyautogui.moveTo(x_coord + x_nudge, y_coord + y_nudge, duration =0.1)



def rangeToDegrees(floor, ceiling, value):
    return round((360 * (value - floor)) / (ceiling - floor))

# Harmonic Product Spectrum (HPS) pitch detection
def hps_pitch(samples, sample_rate):
    # Compute the HPS
    hps = samples[:]
    for i in range(2, 4):  # Adjust the range for better accuracy
        downsampled = samples[::i]
        hps[:len(downsampled)] *= downsampled

    # Find the peak index in HPS
    peak_index = hps.argmax()

    # Convert the index to frequency
    frequency = peak_index * sample_rate / len(samples)

    return frequency

def frequency_to_midi(frequency):
    # Calculate MIDI note number
    midi_note = 69 + 12 * math.log2(frequency / 440)
    return round(midi_note)



#AUDIO INPUT
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 0.1
SAMPLE_SIZE = 10
WAVE_OUTPUT_FILENAME = "output.wav"
FLOOR = 1200
CEILING = 3000

audio = pyaudio.PyAudio()

dirs = {'up': [1500, 20000], 'down': [800, 1499]}

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
recognizer = sr.Recognizer()

while(1):
  samples = []
  for spl in range(SAMPLE_SIZE):
    #print("recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    #print("finish recording")
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    #print(audio.get_sample_size(FORMAT))
    #   waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setsampwidth(2)
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    audio = AudioSegment.from_file(WAVE_OUTPUT_FILENAME, format="wav")
    # Get the pitch (in Hz) using the pydub method
    vol = audio.vol 
    samples.append(vol)
    detected_pitch = hps_pitch(samples, RATE)
    frequency = frequency_to_midi(detected_pitch)
    sample_med = round(statistics.median(samples))
    degrees = rangeToDegrees(FLOOR, CEILING, sample_med)
    print(f"Degrees: {degrees} Median: {sample_med} Pitch: {detected_pitch} Frequency: {frequency}")
  #nudge(20, degrees)
  


  


# Example usage
#hypotenuse = 200  # replace with your actual hypotenuse value
#angle_degrees = 30.0  # replace with your actual angle value
#nudge(hypotenuse, angle_degrees)

#print(f"Length: {length}")
#print(f"Width: {width}")
