# Dev Log:

This document must be updated daily every time you finish a work session.

## Naomi Steinmetz

### 2024-05-14 - Preliminary Researsch
+ did some research and took notes on least bit significance audio steganography: https://medium.com/@AungKyawZall/audio-steganography-39f9fb6d9330, https://anurag219tiwari.medium.com/hiding-in-plain-sight-an-introduction-to-audio-steganography-using-lsb-me-157180aa4027, https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3

### 2024-05-15 - Wave Library
+ read documentation for python wave library: https://docs.python.org/3/library/wave.html

### 2024-05-15 - Other Libraries
+ looked over wave documentation again: https://docs.python.org/3/library/wave.html
+ looked at sys and os libraries and discussed whether to use them: https://docs.python.org/3/library/os.html, https://docs.python.org/3/library/sys.html

### 2024-05-19 - Encode.py
+ started LSB
+ putting modified bytes into a new wav file

### 2024-05-19 - Encode.py debugging
+ helped work out pacing in proposal
+ started debugging encode

### 2024-05-19 - Encode.py additional features
+ added some terminating bits
+ took in multiple data files as input for encode

### 2024-05-20 - audio_modified.wav
+ tested encode
+ fixed output wav file header

### 2024-05-20 - user interface tweaks
+ added option of manual user input for encode
+ changed default embedded audio file name to include name of original file

### 2024-05-21
+ not in class due to AP Macro

### 2024-05-21 - second technique research
+ tested decode.py
+ researched phase coding and tone insertion: https://medium.com/@achyuta.katta/audio-steganography-using-phase-encoding-d13f100380f2, https://www.youtube.com/watch?v=BdEkQ-J76kY, https://scispace.com/pdf/audio-steganography-using-tone-insertion-technique-47rwyqqxh3.pdf

### 2024-05-22
+ not in class due to AP Calc BC

### 2024-05-23
+ not in class due to AP German

### 2024-05-26 - testing lsb
+ added new test cases
+ tested lsb encode and decode
+ fixed file path in decode

### 2024-05-27 - start phase coding
+ researched phase coding: https://arxiv.org/html/2408.13277v2, https://docs.scipy.org/doc/scipy/tutorial/fft.html, https://discuss.pytorch.org/t/equivalent-function-like-numpy-diff-in-pytorch/35327
+ tried to understand templates
+ looked at numpy library

### 2024-05-27 - chunks
+ tried to write chunks for phase coding
+ looked at np.diff, np.fft, pytorch library

### 2024-05-28 - continued phase coding
+ looked at scipy library: https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
+ helped determine if audio was stereo or mono

### 2024-05-28 - phase coding pseudocode
+ tried writing some pseudocode for phase differences in encode.py

### 2024-05-29 - phase encoding
+ looked at tutorial: https://dsp.stackexchange.com/questions/14804/audio-steganography-using-phase-encoding-technique
+ compared tutorial with template

### 2024-05-29 - encoding.py steps 5 and 6
+ tried writing steps 5 and 6 based off of tutorial
+ put comments about step 7

### 2024-05-30 - encode check
+ looked over encode

### 2024-06-01/02 - encode testing/debugging
+ tried to test phase encode with makefile, but problem with importing libraries
+ started decode, added comments

### 2024-06-02 - encode debugging
+ imported Libraries
+ started debugging phase encode

### 2024-06-02/03 - decode start
+ wrote decode outline with comments

### 2024-06-03 - encode testing
+ tested phase encode

### 2024-06-03 - presentation, last minute edits
+ tested phase encode and decode
+ worked on script and presentation slides
+ recorded presentation
