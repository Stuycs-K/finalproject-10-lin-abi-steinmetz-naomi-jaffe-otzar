import wave
import sys

# file_name = "lsb/"+sys.argv[1]
file_name = "data/" + sys.argv[1]

audio = wave.open(file_name, "rb")
num_frames = audio.getnframes()
audio_frames = audio.readframes(num_frames)
frame_bytes = bytearray(list(audio_frames))

decoded_bits = ""
ending = '1111111111111110'

# Get an arr of the last bits
for bit in frame_bytes[45:]:
	last_bit = bit & 3 # changed from 1 to fit 2 lsb per sample
	# decoded_bits += str(int(last_bit))
	decoded_bits += format(last_bit, '02b')

	# Ending
	if len(decoded_bits) > len(ending) and decoded_bits[len(decoded_bits) - len(ending):] == ending:
		decoded_bits = decoded_bits[:len(decoded_bits) - len(ending)]
		break

# Group arr by eights, convert to decimal, then to unicode
decoded_bytes = ""
for i in range(0, len(decoded_bits), 8):
	decoded_bytes += chr(int(decoded_bits[i:i+8],2))

print(decoded_bytes)
