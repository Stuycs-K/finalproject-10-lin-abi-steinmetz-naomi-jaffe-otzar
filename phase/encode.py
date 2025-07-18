import numpy as np
import sys
import math
from scipy.io import wavfile
from typing import Tuple, List
from numpy.typing import NDArray
from pydub import AudioSegment
from io import BytesIO

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

def encode_phase(rate: int, data: NDArray[np.float64], message: str, filename: str) -> None:
	orig_dtype = data.dtype  # remember original dtype
	# determine the type of data (mono or stereo)
	type_of_data = "mono" if len(data.shape) == 1 else "stereo"

	if type_of_data == "stereo":
		print("unsupported audio, converting to mono using BytesIO")
		sound = AudioSegment.from_wav(filename)
		sound = sound.set_channels(1)
		out_io = BytesIO()
		sound.export(out_io, format="wav")
		out_io.seek(0)
		rate, data = wavfile.read(out_io)

	if data.dtype != np.float64:
		data = data.astype(np.float64) # ensure data is in float64 format cause otherwise it breaks when building it back
		print("data type is not float64 so we are converting...")

	num_samples = data.shape[0]
	message_bits = get_bits(message)
	message_len = len(message_bits)
	print("message length in bits:", message_len)

	if message_len == 0:
		print("message is empty")
		return

	if message_len > num_samples // 2:
		print("message is too long for the audio file")
		return

	# Step 1
	sizeOfChunk = math.ceil(num_samples / message_len)

	if sizeOfChunk <= 1:
		print("message is too long for the audio file") # this is because we cannot encode a message that is too long
		return

	data_chunks = []
	for i in range(0, len(data), sizeOfChunk):
		endpoint = i + sizeOfChunk if i + sizeOfChunk < len(data) else len(data)
		chunk = data[i:endpoint]
		if chunk.shape[0] < sizeOfChunk:
			# pad the chunk with zeros if it is smaller than sizeOfChunk
			# numpy.pad(array, pad_width, mode='constant', **kwargs)[source]
			chunk = np.pad(chunk, (0, sizeOfChunk - len(chunk)))
		data_chunks.append(chunk)

	if message_len > len(data_chunks):
		print("message is too long to encode")
		return

	# Step 2
	chunks = []
	for chunk in data_chunks:
		full_ftt = np.fft.fft(chunk)
		mag = abs(full_ftt)
		angle = np.unwrap(np.angle(full_ftt)) # unwrap to prevent certain phase discontinuities
		chunks.append([mag, angle])

	# Step 3
	phase_differences = []
	for i in range(1, len(chunks)):
		phase_differences.append(chunks[i][1] - chunks[i-1][1])

	# Step 4 - only applies to the first block
	phi_list = []
	for d in range(len(message_bits)):
		message_bit = message_bits[d]
		if message_bit == 0:
			phi_list.append(np.pi / 2)
		else:
			phi_list.append(-np.pi / 2)

	# Step 5a
	L = sizeOfChunk
	start = L // 4  # we are now using more stable frequencies cause before it was too close to 0
	m = message_len
	phi_prime = chunks[0][1].copy()
	for i in range(m):
		index_low = start + i
		index_high = L - index_low
		try:
			phi_prime[index_low] = phi_list[i]
			phi_prime[index_high] = -phi_list[i]
		except:
			print("message is too long")
			return
		# make sure magnitude is large enough so phase is stable
		min_amp = 1e-3
		if chunks[0][0][index_low] < min_amp:
			chunks[0][0][index_low] = min_amp
			chunks[0][0][index_high] = min_amp
	chunks[0][1] = phi_prime

	# Step 6
	for i in range(1, len(chunks)):
		chunks[i][1] = chunks[i-1][1] + phase_differences[i-1] # fixed bug here it should be i - 1 not i

	# Step 7
	# put the thing back into chunks, reconstruct the thing
	new_chunks = []
	for mag, angle in chunks:
		complex = mag * np.exp(1j * angle)
		chunk = np.fft.ifft(complex)
		real_chunk = np.real(chunk)
		# make sure the chunk is in the float64 format or else it breaaks
		real_chunk = real_chunk.astype(np.float64)
		new_chunks.append(real_chunk)

	# creating the channel array
	channels = []
	for chunk in new_chunks:
		channels.extend(chunk)
	channels = np.array(channels)

	# Step 8a - make it not super loud
	peak_orig = np.max(np.abs(data))
	peak_mod = np.max(np.abs(channels))
	if peak_mod > 0:
		scale = peak_orig / peak_mod
		channels = channels * scale

	# Step 8b - convert back to original dtype for writing
	"""print(type(channels[0]))
	print(orig_dtype)
	channels = channels.astype(orig_dtype)"""

	# Step 8c
	mod_name = filename[0:len(filename)-4] + "_modified.wav"
	wavfile.write(mod_name, rate, channels)

if __name__ == "__main__":
	file = sys.argv[1]
	message = sys.argv[2]

	rate, data = read_file(file)

	print("encoding message:", message)
	encode_phase(rate, data, message, file)
	print("done")
