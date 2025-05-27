import wave
import numpy as np
import sys
import struct

file = sys.argv[1]
message = sys.argv[2]

# 1: read file
audio = wave.open(file, "rb")
parameters = audio.getparams()
num_channels = audio.getnchannels()
sample_width = audio.getsampwidth()
num_frames = audio.getnframes()
num_samples = num_frames * num_channels
audio_frames = audio.readframes(num_frames)
frame_bytes = bytearray(list(audio_frames)) #convert song to byte array

# 2: get the samples
samples = []
for i in range(0, len(frame_bytes), 2):
	samples.append(int.from_bytes(frame_bytes[i: i+2], byteorder="little", signed=True))

print(num_samples)
print(len(samples))

# 3: message bits
message_bits = []
for i in message:
	byte = ord(i)
	# convert to binary and get a string
	raw_binary = str(bin(byte)[2:].zfill(8))
	for j in raw_binary:
		message_bits.append(int(j))

samples = np.fft.fft(samples)

for i in range(num_samples):
	pass	

samples = np.fft.ifft(samples)
