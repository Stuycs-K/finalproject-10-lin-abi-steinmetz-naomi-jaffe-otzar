import wave
import sys

file_name = sys.argv[1]

audio = wave.open(file_name, "rb")
num_frames = audio.getnframes()
audio_frames = audio.readframes(num_frames)
frame_bytes = bytearray(list(audio_frames))

decoded_bits = []

# Get an arr of the last bits
for bit in frame_bytes:
	last_bit = bit & 1
	decoded_bits.append(int(last_bit))

# Group arr by eights
decoded_bytes = []
for i in range(0, len(decoded_bits) // 8, 8):
	decoded_bytes.append()
