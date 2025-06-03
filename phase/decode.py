import numpy as np
import sys
import struct
import math
from scipy.io import wavfile
from typing import Tuple, List
from numpy.typing import NDArray

file = sys.argv[1]
print("What is the length of the message encoded? ")
message_len = int(round(float(input())))

def read_file(file: str) -> Tuple[int, NDArray[np.float64]]:
	return wavfile.read(file)

decoded_bits = ""

rate, data = read_file(file)

type_of_data = "mono" if len(data.shape) == 1 else "stereo"

if type_of_data == "mono":
    num_samples = data.shape[0]

    # Step 1: making chunks
    sizeOfChunk = math.ceil(num_samples / message_len)

    data_chunks = []
    for i in range(0, len(data), sizeOfChunk):
        endpoint = i + sizeOfChunk if i + sizeOfChunk < len(data) else len(data)
        chunk = data[i:endpoint]
        if chunk.shape[0] < sizeOfChunk:
            # pad the chunk with zeros if it is smaller than sizeOfChunk
            # numpy.pad(array, pad_width, mode='constant', **kwargs)[source]
            chunk = np.pad(chunk, (0, sizeOfChunk - len(chunk)))
        data_chunks.append(chunk)

    # Step 2
    info = []
    for chunk in data_chunks:
        full_ftt = np.fft.fft(chunk)
        mag = abs(full_ftt)
        angle = np.unwrap(np.angle(full_ftt)) # unwrap to prevent certain phase discontinuities
        info.append([mag, angle])

    # Step 3
    phase_differences = []
    for i in range(1, len(info)):
        info[i][1] = info[i][1] - info[i-1][1]
        phase_differences.append(info[i][1])

    # Step 4
    phi_prime = []
    info[0][1] = phi_prime
    phi_list = []

    L = sizeOfChunk
    m = message_len

    for i in range(message_len):
        index = L // 2 + (m - i)
        phi_list[i] = -phi_prime[index]

    phi_prime = info[0][1].copy()
    for i in range(message_len):
        index = (L//2 - m) + i
        # phi_prime[index] += phi_list[i] #how do we get phi_list[i] from this? do we subtract phase difference or something?

    for bit in phi_list:
        if phi_list[bit] == np.pi/2:
            decoded_bits += "0"
        else:
            decoded_bits += "1"

    # taken from other decode (was unsure if ending part should be put in too)
    # Group arr by eights, convert to decimal, then to unicode
    decoded_bytes = ""
    for i in range(0, len(decoded_bits), 8):
        decoded_bytes += chr(int(decoded_bits[i:i+8],2))

    print(decoded_bytes)
