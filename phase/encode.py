import numpy as np
import sys
import struct
import math
from scipy.io import wavfile
from typing import Tuple, List
from numpy.typing import NDArray

file = sys.argv[1]
message = sys.argv[2]

def read_file(file: str) -> Tuple[int, NDArray[np.float64]]:
	return wavfile.read(file)

def get_bits(message: str) -> List[int]:
	message_bits = []
	for i in message:
		byte = ord(i)
		# convert to binary and get a string
		raw_binary = str(bin(byte)[2:].zfill(8))
		for j in raw_binary:
			message_bits.append(int(j))
	return message_bits

rate, data = read_file(file)

def encode_phase(rate: int, data: NDArray[np.float64], message: str) -> None:
	# determine the type of data (mono or stereo)
	type_of_data = "mono" if len(data.shape) == 1 else "stereo"

	if type_of_data == "mono":
		num_samples = data.shape[0]
		message_bits = get_bits(message)
		message_len = len(message_bits)

		# Step 1
		sizeOfChunk = math.ceil(num_samples / message_len)
		numChunks = math.ceil(len(data) / sizeOfChunk)

		data_chunks = []
		for i in range(0, len(data), sizeOfChunk):
			endpoint = i + sizeOfChunk if i + sizeOfChunk < len(data) else len(data)
			data_chunks.append(data[i:endpoint])

		# Step 2
		info = []
		for chunk in data_chunks:
			mag = abs(np.fft.fft(chunk))
			angle = np.angle(np.fft.fft(chunk))
			info.append((mag, angle))

		# Step 3
		phase_differences = []
		for i in range(1, len(info)):
			phase_differences.append(info[i][1] - info[i-1][1])

		# Step 4
		phi_list = []
		for i in range(len(info)):
			message_bit = message_bits[i]
			if message_bit == 0:
				phi_list.append(np.pi / 2)
			else:
				phi_list.append(-np.pi / 2)

		# Step 5a SOMEONE PLEASE CHECK EVERY STEP FROM THIS ONE ON (；人；)
		for i in range(message_len):
			info[sizeOfChunk/2 - message_len + i][1] = phi_list[i]

		# Step 5b
		for i in range(message_len):
			info[sizeOfChunk/2 + 1 + i][1] = phi_list[message_len + 1 - i]

		# Step 6
		for i in range(2, numChunks):
			info[i][1] = info[i-1][1] + phase_differences[i]

		chunks = []

		# Step 7
		# wth does Aiexp(jphasei) mean????
		# put the thing back into chunks, reconstruct signal
		chunks = np.fft.ifft(chunks)
		channels = []
		for chunk in chunks:
			channels.extend(chunk)

		# Step 8
		wavefile.write("steg", rate, channels)
	else:
		print("stereo audio not supported yet")

if __name__ == "__main__":
	print("encoding message:", message)
	encode_phase(rate, data, message)
	print("done")