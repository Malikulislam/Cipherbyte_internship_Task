import sounddevice as sd
import wavio



# Set the recording parameters
fs = 44100  # Sample rate
duration = 10  # Duration of recording in seconds

# Record audio
print("Recording audio...")
try:
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
except sd.PortAudioError as e:
    print(f"Error recording audio: {e}")

# Save the recorded audio to a WAV file
wavio.write("recorded_audio.wav", audio, fs, sampwidth=2)

# Play the recorded audio
print("Playing audio...")
try:
    sd.play(audio, fs)
    sd.wait()  # Wait until playback is finished
    print("Audio finished.")
except sd.PortAudioError as e:
    print(f"Error playing audio: {e}")