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
            chunk = np.pad(chunk, (0, sizeOfChunk - len(chunk)))
        data_chunks.append(chunk)

    # Step 2: compute FFT of the first chunk to read encoded bits
    full_fft = np.fft.fft(data_chunks[0])
    L = sizeOfChunk
    start_bin = L // 4 # we are now using more stable frequencies cause before it was too close to 0

    phases = []
    for i in range(message_len):
        index = L - (start_bin + i)
        phase = np.angle(full_fft[index])
        phases.append(phase)

    for phase in phases:
        if phase < 0:
            decoded_bits += "0"
        else:
            decoded_bits += "1"

    # taken from other decode (was unsure if ending part should be put in too)
    # Group arr by eights, convert to decimal, then to unicode
    decoded_bytes = ""
    for i in range(0, len(decoded_bits), 8):
        decoded_bytes += chr(int(decoded_bits[i:i+8],2))

    print(decoded_bytes)
else:
    print("only mono data supported.")
