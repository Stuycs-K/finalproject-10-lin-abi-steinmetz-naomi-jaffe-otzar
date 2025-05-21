import wave
import os
import struct
import sys



def encoding(fileList):
    if (len(fileList) < 2):
        print("Invalid arguments")
        return "false"
    audiofile = fileList[1]
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
    for f in range(2,len(fileList)):
        message = fileList[f]

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
        return "false"

    i = 45
    for bit in msg_bin:
        if (i > len(frame_bytes)-1):
            print("incomplete encoding")
            break
        frame_bytes[i] = (frame_bytes[i] & 254)|int(bit)
        i+=1

    for x in range(8):
        if (i <= len(frame_bytes)-1):
            frame_bytes[i] = (frame_bytes[i] & 254)|1
        i+=1

    new_frames = bytes(frame_bytes) #look into whether this is necessary

    mod_name = audiofile[0:len(audiofile)-4] + "_modified.wav"

    with wave.open(mod_name, "wb") as song:
        # song.setcomptype(parameters)
        song.setparams(parameters)
        song.writeframes(new_frames)

    return "true"

# command line arguments
if len(sys.argv) >= 3:
    # print("Usage: make encode ARGS=\"<audiofile.wav> <message1.txt> <message2txt> ...\"")
    success = encoding(sys.argv)
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
success = encoding(arglist)
if (success == "false"):
    print("please try again")
    exit()
print("embedded audio available")
exit()