# Dev Log:

This document must be updated daily every time you finish a work session.

## Abigail Lin

### 2024-05-15 - Preliminary Research on Audio Stegnography
Research how to code LSB in audio stegnography, figuring out the best programming language to use (python). Similarly to image stegnography, we will be converting the audio file into a bit stream, where it will be manipulated to store a secret message.

### 2024-05-16 - Planning implmentation from WAV to bite stream
Looked at example projects that simiarly using LSB in audio stegnography with python. Found examples of command line arguments we could implement: hide data, recover data, input file, secret message file, output file, how many LSBs to use, and how many bytes to recover from the sound. Will implement the conversion of wave file to bit stream.

HOMEWORK:
Used examples and documentation to implement first steps of processing a wav file, and retrieving neccessary parameters. Also, taking in the hidden message and converting to binary. Tested, and printed with print statements, added example audio.wav, data.txt, and makefile to include python3 and python. Included struct, but needs more research to fully understand LSB implementation.
