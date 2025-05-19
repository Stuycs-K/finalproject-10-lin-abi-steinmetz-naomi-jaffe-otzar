import wave
import os

# open cover audio file, retrieve parameters -> convert to binary string of bits (later)
audio = wave.open("audio.wav", "rb")
parameters = audio.getparams()
num_channels = audio.getnchannels()
sample_width = audio.getsampwidth()
num_frames = audio.getnframes()
num_samples = num_frames * num_channels
audio_frames = audio.readframes(num_frames)
print("parameters: ", parameters)
print("num of audio samples: ", num_samples)

# read the message
with open("data.txt", "r") as file:
    msg = file.read()
print("message read: ",msg)

# convert the message to binary
msg_bin = ''.join(format(ord(c), '08b') for c in msg)
print("message in binary: ",msg_bin)