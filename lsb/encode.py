import wave
import os
import struct
import sys



def check_flip(data, a, b): # part of LSB flip, which modifies 3rd + 4th LSB, and changes it based on pattern
    store = data & 12 # 3rd and 4th bits
    if store == 0 and (a == 0 and b == 0):
        return data
    elif store == 4 and (a == 0 and b == 1):
        return data
    elif store == 8 and (a == 1 and b == 0):
        return data
    elif store == 12 and (a == 1 and b == 1):
        return data
    else:
        return data ^ 3


def encoding(fileList, mode, output_name = None):
    if (len(fileList) < 2):
        print("Invalid arguments")
        return "false"
    audiofile = "data/"+fileList[1]
    # open cover audio file, retrieve parameters -> convert to binary string of bits (later)
    audio = wave.open(audiofile, "rb")
    parameters = audio.getparams()
    num_channels = audio.getnchannels()
    print("num of channels", num_channels)
    sample_width = audio.getsampwidth()
    num_frames = audio.getnframes()
    num_samples = num_frames * num_channels
    audio_frames = audio.readframes(num_frames)
    frame_bytes = bytearray(list(audio_frames)) #convert song to byte array
    # print("parameters: ", parameters)
    # print("num of audio samples: ", num_samples)

    msg = ""
    for f in range(2,len(fileList)):
        message = "data/"+fileList[f]

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
    # print("message in binary: ",msg_bin)

    if mode == "1" and msg_len > len(frame_bytes):
        print("message too large to encode in audio file (1-bit LSB)")
        return "false"
    if (mode == "2" or mode == "flip") and msg_len > len(frame_bytes) * 2:
        print("message too large for audio file (2-bit/flip mode)")
        return "false"
    # msg_len_bits = len(msg_bin)
    # length_bytes = struct.pack('>I', msg_len_bits)
    # length_bits = ''.join(format(b, '08b') for b in length_bytes)

    i = 45
    # 2 LSB per sample / flip mode
    if mode in ["2", "flip"] and len(msg_bin) % 2 != 0:
        msg_bin += '0'

    if mode == "1":
        for bit in msg_bin:
            if (i > len(frame_bytes)-1):
                print("incomplete encoding")
                break
            frame_bytes[i] = (frame_bytes[i] & 254)|int(bit)
            i+=1
    elif mode == "2":
        for j in range(0, len(msg_bin), 2):
            if i > len(frame_bytes) - 1:
                print("incomplete encoding")
                break
            two_bits = msg_bin[j:j+2]
            two_bits_val = int(two_bits, 2)
            frame_bytes[i] = (frame_bytes[i] & 252)| two_bits_val # clears last 2 bits
            i+= 1
    elif mode == "flip":
        for j in range(0, len(msg_bin), 2):
            if i > len(frame_bytes) - 1:
                print("incomplete encoding")
                break
            a = int(msg_bin[j])
            b = int(msg_bin[j+1])
            frame_bytes[i] = check_flip(frame_bytes[i], a, b)
            frame_bytes[i] = frame_bytes[i] & 243  # clear bits 3 and 2
            if a == 0 and b == 0:
                frame_bytes[i] += 0
            elif a == 0 and b == 1:
                frame_bytes[i] += 4
            elif a == 1 and b == 0:
                frame_bytes[i] += 8
            elif a == 1 and b == 1:
                frame_bytes[i] += 12
            i += 1
    else:
        print("invalid encoding mode selected")
        return "false"

    new_frames = bytes(frame_bytes)

    if output_name is None:
        mod_name = audiofile[0:len(audiofile)-4] + "_modified.wav"
    else:
        if not output_name.endswith(".wav"):
            output_name += ".wav"
        mod_name = "data/"+output_name

    with wave.open(mod_name, "wb") as song:
        song.setparams(parameters)
        song.writeframes(new_frames)

    return "true"

# print("Usage: make encode ARGS=\"<audiofile.wav> <message1.txt> <message2txt> ...\"")
# command line arguments
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

print("Please enter the name of the output file: ")
output_name = input()
if output_name.strip() == "":
    output_name = None
success = encoding(arglist, mode, output_name)

if (success == "false"):
    print("please try again")
    exit()
print("embedded audio available")
exit()
