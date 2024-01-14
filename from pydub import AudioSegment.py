from pydub import AudioSegment
from pydub.playback import play

# Load an audio file (replace 'your_audio_file.wav' with the actual path to your audio file)
audio = AudioSegment.from_wav('your_audio_file.wav')

# Set up pitch detection
pitch = audio.dBFS  # set reference pitch (you can experiment with this value)
samples = audio.get_array_of_samples()

# Find the pitch
detected_pitch = samples.index(max(samples))  # this is a simple example, not accurate pitch detection

# Print the detected pitch (this will be an index, not a MIDI note)
print(f"Detected Pitch: {detected_pitch}")

# Convert the index to a frequency (you may need a more sophisticated method for accurate pitch conversion)
frequency = detected_pitch / len(samples) * audio.frame_rate
print(f"Frequency: {frequency} Hz")