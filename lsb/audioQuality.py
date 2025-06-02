import wave
import os
import struct
import sys

def getSample(wav_file):
    with wave.open(wav_file, 'rb') as audio:
        num_frames = audio.getnframes()
        sample_width = audio.getsampwidth()
        raw_frames = audio.readframes(num_frames)

        samples = []
        for i in range(0, len(raw_frames), sample_width):
            sample = struct.unpack('<h', raw_frames[i:i+2])[0] # convert raw bytes into a signed integer
            samples.append(sample)
    return samples

# SNR = signal to noise ratio
def signalNoiseRatio(original_sample, modified_sample):
    signal_power = 0
    noise_power = 0
    