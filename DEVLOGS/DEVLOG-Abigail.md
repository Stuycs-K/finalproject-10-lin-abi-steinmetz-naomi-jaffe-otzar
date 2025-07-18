# Dev Log:

This document must be updated daily every time you finish a work session.

## Abigail Lin

### 2024-05-15 - Preliminary Research on Audio Stegnography
Research how to code LSB in audio stegnography, figuring out the best programming language to use (python). Similarly to image stegnography, we will be converting the audio file into a bit stream, where it will be manipulated to store a secret message.

### 2024-05-16 - Planning implmentation from WAV to bite stream
Looked at example projects that simiarly using LSB in audio stegnography with python. Found examples of command line arguments we could implement: hide data, recover data, input file, secret message file, output file, how many LSBs to use, and how many bytes to recover from the sound. Will implement the conversion of wave file to bit stream.

**HOMEWORK:**\
Used examples and documentation to implement first steps of processing a wav file, and retrieving neccessary parameters. Also, taking in the hidden message and converting to binary. Tested, and printed with print statements, added example audio.wav, data.txt, and makefile to include python3 and python. Included struct, but needs more research to fully understand LSB implementation.

### 2024-05-19 - Finishing encode.py, working on proposal
Discussed with groupmates on proposal, including how the work will be split up, and what our expected due dates for each part of the process will be. Researched a bit to see if there were any more parts of the class that we could implemment into our project. Worked with Naomi to run and debug encode.py

**HOMEWORK:**\
Updated encode.py and makefile to include command line arguments, which now take an audiofile and secret message. After looking at Otzar's temporary decode, added a terminator to aid. Fixed bug by changing setcompytype to setparams as setcomptype ran into a bug with a TypeError. Looking into increasing LSb per sample.

### 2024-05-19 - Testing encode.py & decode.py together, working on enhancing LSB
In class, worked with groupmates to explain what we did in our respective roles of encode.py and decode.py, and testing what worked. We found a few problems concerning the header and the terminating characters, which we were able to fix, though more testing is needed.

At home, working on enhancing the current LSB to store with 2 bytes instead of 1 byte for a more undetectable way of hiding messages. This should come out with slighter worse audio, but a higher chance of remaining undetected versus the classic 1 byte LSB method. Need to test with decode, but similar code instead clearing and using the last 2 bits.

### 2024-05-21 - Finishing LSB 2 byte method
Out for AP Macro.

At home, tested current decode.py. Had to debug and remove some code from the prior 1 LSB that was messing up the code, and adjust decoder slightly to accomodate for the new LSB 2 byte method. Tested and finished.

### 2024-05-22 - Starting LSB with Flipper method
Out for AP Calc BC.

At home, started working on LSB with flipper, which will take the 3rd and 4th bits of each audio byte, and only change them if they match certain conditions. Created check_flip function.

### 2024-05-23 - Updating User UI
In class, Otzar updated the organization by putting everything into files. I updated encode.py and decode.py so that it properly accounts for this, and can be run in the general folder.

At home, continuied to improve on the user input. Makefile is now properly updated. Finished flipper mode, and updated the user input so that it can switch between 1-bit, 2-bit, and now 2-bit with flipper. Added user-input to decode.py as well.


### 2024-05-27 - Updating README.md and writing script for presentation
In class, worked on re-reading the articles and resources we used in our research to compile into a readable format for our README.md and script presentation. All work on google doc.

At home, finished up README.md script, will be importing it into the file along with links and images tommorow.

At home, continuing to add to sources and outside uses of audio stegography with images and article sources. All work on google doc.

### 2024-05-28 - Updating README.md and writing script for presentation
In class, was updated on Naomi and Otzar's progress on phase coding. Continued to add to google doc of compiling research and presentation script.

At home, continued to work on finishing up research and presentation script.

### 2024-05-29 - Reviewing markdown and transferring google doc to README.md
In class, finished the project overview of the README.md, adding all relevant images and links.

At home, finished project usage in the README.md, and learned about potential extra code for analyzing the accuracy of the audio changes. Researched and prepared to code.

### 2024-05-30 - Finished sources, reviewed phase coding, started on audio quality comparison
In class, finished up the README.md by adding relevant sources. Reviewed phase coding in class with Otzar and Naomi. Started researching audio quality comparison.

At home, continued research into audio quality comparison, decided to use signal to noise ratio to compare the original and modified audio.

### 2024-06-02 - Working on compare audio function
In class, continued work on implementing research on Signal-to-Noise Ratio (SNR) in python to be used as a comparison between the original and modified audio to see how distorted it became. Finished most of code, but needed to add user input.

At home, cleaned up the code and added user input + into makefile to be used. Did testing with the audio with the three different modes, which correctly shows that with each mode increasing, the signal-to-noise ratio lowers in dB. Need to update code to allow for output file name.
