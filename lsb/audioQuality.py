import wave
import os
import struct
import sys
import numpy as np
from scipy.io import wavfile

print("Choose decoding mode:")
print("1 = 1-bit LSB")
print("2 = 2-bit LSB")
print("flip = 2 bit (bits 3 and 2) + optional flip of bits 1 and 0")
mode = input("Enter mode (1/2/flip): ")

file_name = "data/"+sys.argv[1]

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
    count = min(len(samples1), len(samples2))
    for i in range(count):
        signal_power += samples1[i] ** 2
        noise_power += (samples1[i] - samples2[i]) ** 2
    signal_power /= count
    noise_power /= count

    if noise_power == 0:
        return float('inf')  # perfect match
    snr = 10 * math.log10(signal_power / noise_power)
    return snr

# def calculateSNR(original_audio, modified_audio):
#     originalData =  wavefile.read(original_audio)
#     modifiedData = wavefile.read(modified_audio)

if len(sys.argv) >= 3:
    print("Choose encoding mode:")
    print("1 = 1-bit LSB")
    print("2 = 2-bit LSB")
    print("flip = 2 bit (bits 3 and 2) + optional flip of bits 1 and 0")
    mode = input("Enter mode (1/2/flip): ")
    success = encoding(sys.argv, mode)
    if (success == "false"):
        print("please try again")
        exit()
    print("embedded audio available")
    exit()

print("Please enter the name of the audio file (must be a wave file): ")
audiofile = input()
while (not(audiofile.endswith(".wav"))):
    print("Please try again. The file must end in .wav: ")
    audiofile = input()
arglist = [""]
arglist.append(audiofile)

print("Please enter the (first) file containing the secret message: ")
fileName = input()
arglist.append(fileName)
while (True):
    print("Would you like to add another secret message? (y/n)")
    cont = input()
    if (cont == "n"):
        break
    print("Please enter file name: ")
    fileName = input()
    arglist.append(fileName)

print("Choose encoding mode:")
print("1 = 1-bit LSB")
print("2 = 2-bit LSB")
print("flip = 2 bit (bits 3 and 2) + optional flip of bits 1 and 0")
mode = input("Enter mode (1/2/flip): ")

success = encoding(arglist, mode)
if (success == "false"):
    print("please try again")
    exit()
print("embedded audio available")
exit()
