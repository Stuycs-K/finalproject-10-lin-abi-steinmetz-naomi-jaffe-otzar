import wave
import os
import struct
import sys

# command line arguments
if len(sys.argv) < 3:
    print("Usage: make encode ARGS=\"<audiofile.wav> <message1.txt> <message2txt> ...\"")
    exit()

audiofile = sys.argv[1]
# open cover audio file, retrieve parameters -> convert to binary string of bits (later)
audio = wave.open(audiofile, "rb")
parameters = audio.getparams()
num_channels = audio.getnchannels()
sample_width = audio.getsampwidth()
num_frames = audio.getnframes()
num_samples = num_frames * num_channels
audio_frames = audio.readframes(num_frames)
frame_bytes = bytearray(list(audio_frames)) #convert song to byte array
print("parameters: ", parameters)
print("num of audio samples: ", num_samples)

msg = ""
for f in range(2,len(sys.argv)):
    message = sys.argv[f]

    # read the message
    with open(message, "r") as file:
        msg += file.read()
    print("message read: ",msg)

# convert the message to binary
msg_bin = ''.join(format(ord(c), '08b') for c in msg)
# delimiter so decoder knows when to stop (for decoding, can delete)
terminate = '1111111111111110'
msg_bin += terminate

msg_len = len(msg_bin)
print("message in binary: ",msg_bin)


# 1 LSB per sample -> can ramp up to 2 or 4 LSB
if msg_len > len(frame_bytes):
    print("message is too large to encode in audio file")
    exit()

i = 0
for bit in msg_bin:
    frame_bytes[i] = (frame_bytes[i] & 254)|int(bit)
    i+=1
    if (i > len(frame_bytes)-1):
        print("incomplete encoding")
        break

# for x in range(8):
#     if (i <= len(frame_bytes)-1):
#         frame_bytes[i] = (frame_bytes[i] & 254)|1
#     i+=1

new_frames = bytes(frame_bytes) #look into whether this is necessary

with wave.open("audio_modified.wav", "wb") as song:
    # song.setcomptype(parameters)
    song.setparams(parameters)
    song.writeframes(new_frames)

print("embedded audio available")
