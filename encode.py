import wave
import os
import struct

# open cover audio file, retrieve parameters -> convert to binary string of bits (later)
audio = wave.open("audio.wav", "rb")
parameters = audio.getparams()
num_channels = audio.getnchannels()
sample_width = audio.getsampwidth()
num_frames = audio.getnframes()
num_samples = num_frames * num_channels
audio_frames = audio.readframes(num_frames)
frame_bytes = bytearray(list(audio_frames)) #convert song to byte array
print("parameters: ", parameters)
print("num of audio samples: ", num_samples)

# read the message
with open("data.txt", "r") as file:
    msg = file.read()
print("message read: ",msg)

# convert the message to binary
msg_bin = ''.join(format(ord(c), '08b') for c in msg)
msg_len = len(msg_bin)
print("message in binary: ",msg_bin)
print("message in binary printing bits:")
for t in msg_bin:
    print(" ",int(t))


# 1 LSB per sample? need to check if can fit into audio
i = 0
for bit in msg_bin:
    frame_bytes[i] = (frame_bytes[i] & 254)|int(bit)
    i+=1
    if (i > len(frame_bytes)-1):
        print("incomplete encoding")
        break
# LSB code

new_frames = bytes(frame_bytes) #look into whether this is necessary

with wave.open("audio_modified.wav", "wb") as song:
    song.setcomptype(parameters)
    song.writeframes(new_frames)

print("embedded audio available")
