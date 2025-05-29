import wave
import numpy as np
import sys
import struct
import math
from scipy.io import wavfile
from scipy.fft import fft, ifft
from typing import List

file = sys.argv[1]
message = sys.argv[2]

# 1: read file
def read_file(file: str) -> List[int, np.arr]:
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
def get_bits(message: str) -> List[int]:
	message_bits = []
	for i in message:
		byte = ord(i)
		# convert to binary and get a string
		raw_binary = str(bin(byte)[2:].zfill(8))
		for j in raw_binary:
			message_bits.append(int(j))
	return message_bits

samples = np.fft.fft(samples)

for i in range(num_samples):
	pass	

rate, data = wavefile.read(file)
num_samples = len(data)
message_bits = get_bits(message)
message_len = len(message_bits)
sizeOfChunk = math.celi(num_samples / message_len)
numChunks = math.ceil(len(data) / sizeOfChunk)

data_chunks = []
for i in range(0, len(data), sizeOfChunk):
	endpoint = i + sizeOfChunk if i + sizeOfChunk < len(data) else len(data)
	data_chunks.append(data[i:endpoint])
	
info = []
for chunk in data_chunks:
	mag = abs(np.fft.ftt(chunk))
	angle = np.angle(np.fft.fft(chunk))
	info.append((mag, angle))

phase_differences = []
for i in range(1, len(info)):
	phase_differences.append(info[i][1] - info[i-1][1])

phi_list = []
for i in range(len(info)):
	message_bit = message_bits[i]
	if message_bit == 0:
		phi_list.append(np.pi / 2)
	else:
		phi_list.append(-np.pi / 2)



#samples = np.fft.ifft(samples)

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
