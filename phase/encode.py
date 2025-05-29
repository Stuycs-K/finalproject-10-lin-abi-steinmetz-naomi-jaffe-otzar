import wave
import numpy as np
import sys
import struct
# import math
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

# must find chunksize: example uses np code  
# "The expression 2 * 2 ** np.ceil(np.log2(2 * textLength)) calculates the smallest power of 2 that is greater than or equal to 2 * textLength, and then multiplies the result by 2. Here's how it breaks down"

# for i in samples:
# 	i = abs(fft(i))
# 	i = np.angle(i) #idk if we can get around the use of np here

# diff_samples = [samples[i+1] - samples[i] for i range(len(arr) - 1)] 

# converting message to phase diffs
# message_bits[message_bits == 0] = -1
# message_bits *= -math.pi/2

# phase conversion
# 