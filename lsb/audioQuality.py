import wave
import os
import struct
import sys
import math

def getSamples(wav_file):
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
    count = min(len(sample1), len(sample2))
    for i in range(count):
        signal_power += sample1[i] ** 2
        noise_power += (sample1[i] - sample2[i]) ** 2
    signal_power /= count
    noise_power /= count

    if noise_power == 0: # same audio
        return "infinite"
    snr = 10 * math.log10(signal_power / noise_power)
    return snr

print("Please enter the original audio file name (must be a wave file):")
originalfile = input()
while (not(originalfile.endswith(".wav"))):
    print("Please try again. The file must end in .wav: ")
    originalfile = input()

print("Please enter the modified audio file name (must be a wave file):")
modifiedfile = input()
while (not(modifiedfile.endswith(".wav"))):
    print("Please try again. The file must end in .wav: ")
    modifiedfile = input()

originalfile = "data/"+originalfile
modifiedfile = "data/"+modifiedfile

sample1 = getSamples(originalfile)
sample2 = getSamples(modifiedfile)

snr_value = f"{signalNoiseRatio(sample1, sample2):.2f}"
print(f"\nSignal-to-Noise Ratio (SNR): "+snr_value+" dB")