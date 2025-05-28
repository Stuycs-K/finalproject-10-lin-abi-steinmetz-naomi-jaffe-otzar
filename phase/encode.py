import wave
import numpy as np
import sys
import struct
from scipy.io import wavfile
from scipy.fft import fft, ifft
from typing import List

file = sys.argv[1]
message = sys.argv[2]

# 1: read file
def read_file(file: str): -> List[int, np.arr]
	return rate, data = wavefile.read(file)

# 2: get the samples
def get_samples():
	samples = []
	for i in range(0, len(frame_bytes), 2):
		samples.append(int.from_bytes(frame_bytes[i: i+2], byteorder="little", signed=True))

	print(num_samples)
	print(len(samples))

	return samples

# 3: message bits
def get_bits():
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

# for i in samples:
# 	i = abs(fft(i))
# 	i = np.angle(i) #idk if we can get around the use of np here

# diff_torch = [samples[i+1] - samples[i] for i range(len(arr) - 1)] 
