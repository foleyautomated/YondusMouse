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

