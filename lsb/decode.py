import wave
import sys

print("Choose decoding mode:")
print("1 = 1-bit LSB")
print("2 = 2-bit LSB")
print("flip = 2 bit (bits 3 and 2) + optional flip of bits 1 and 0")
mode = input("Enter mode (1/2/flip): ")

file_name = "data/"+sys.argv[1]

audio = wave.open(file_name, "rb")
num_frames = audio.getnframes()
audio_frames = audio.readframes(num_frames)
frame_bytes = bytearray(list(audio_frames))

decoded_bits = ""
ending = '1111111111111110'

# Get an arr of the last bits
for byte in frame_bytes[45:]:
	if mode == "1":
		last_bit = byte & 1
		decoded_bits += str(last_bit)
	elif mode == "2":
		two_bits = byte & 3
		decoded_bits += format(two_bits, '02b')
	elif mode == "flip":
		flip_bits = (byte & 12) >> 2 # bits 3 and 2 (1100)
		decoded_bits += format(flip_bits, '02b')
	else:
		print("invalid decoding mode")
		exit()

	# Ending
	if len(decoded_bits) > len(ending) and decoded_bits[len(decoded_bits) - len(ending):] == ending:
		decoded_bits = decoded_bits[:len(decoded_bits) - len(ending)]
		break

# Group arr by eights, convert to decimal, then to unicode
decoded_bytes = ""
for i in range(0, len(decoded_bits), 8):
	decoded_bytes += chr(int(decoded_bits[i:i+8],2))

print(decoded_bytes)
