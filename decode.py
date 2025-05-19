import wave
import sys

file_name = sys.argv[1]

audio = wave.open(file_name, "rb")
num_frames = audio.getnframes()
audio_frames = audio.readframes(num_frames)
frame_bytes = bytearray(list(audio_frames))
