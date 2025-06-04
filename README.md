[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/am3xLbu5)
# Audio Stegonography
 
### Group Name: CITY HALL DAD LEGS

**Group Members:** Abigail Lin, Naomi Steinmetz, Otzar Jaffe
       
## Project Description:

Audio Steganography refers to the art of hiding information in audio files. This is different from encryption, as it relies on the assumption that people won’t know to look for the secret message in the chosen vector, which is audio.

This has applications beyond allowing for simple messages to be sent like most other common encryption methods. It can be used to:
1. **[Track User Data](https://arstechnica.com/information-technology/2017/05/theres-a-spike-in-android-apps-that-covertly-listen-for-inaudible-sounds-in-ads/)**
   1. App developer SilverPush used inaudible sound in TV commercials to track phone users. The beacons were frequencies from 18kHz to 20kHz, a range which is inaudible to most humans, but is easy to detect by phone microphones. With audio steganography, shopping companies use the location of a shopper to promote certain products.
2. **[Hide Malware](https://cisomag.com/hackers-using-steganography-in-wav-audio-files-to-hide-malware/)**
   1. Research shows that hackers are using WAV audio files to hide malware like crypto miner script “XMRig Monero CPU” miner and “Metasploit” code to gain remote access to victims.
3. **[Trigger Smart Home Devices](https://www.theverge.com/2018/2/2/16965484/amazon-alexa-super-bowl-ad-activate-frequency-commercial-echo)**
   1. Speculation on Alexa not responding to Super Bowl Ads indicate that Amazon took advantage of the frequency range of their ads to stop Alexa from responding. In a [paper](http://www.theregister.com/2018/01/11/ai_adversarial_attack_speech_recognition/), small changes to a waveform in audio in a speech engine can return a different result than what a human would expect.

In our first method in tackling audio steganography, we decided to use a Least Significant Bit (LSB) algorithm. This works by converting the audio (a .wav file) into bytes, and changing the least significant bit of each byte with a bit from the message file.

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*THFuhBPeMI5lE4JiLcF-OQ.png)

In order to extract the data, the decoder will take the least significant bit from each byte of the audio and reconstruct the message.

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*7ElCrXNicOSyqXdD9XMy3w.png)

In our python implementation, we will use bit manipulation tool AND with a bit mask (254) to clear the least significant bit of the audio byte. Then, we can use the tool OR and attach the bit of the secret message to the audio byte.

![](https://github.com/Stuycs-K/finalproject-10-lin-abi-steinmetz-naomi-jaffe-otzar/blob/main/images/image2.jpg)
![](https://github.com/Stuycs-K/finalproject-10-lin-abi-steinmetz-naomi-jaffe-otzar/blob/main/images/image1.jpg)
  
## Instructions:

In order to run this project, you must have Python installed.
1. **Clone the repository:**
```bash
git clone git@github.com:Stuycs-K/finalproject-10-lin-abi-steinmetz-naomi-jaffe-otzar.git
cd finalproject-10-lin-abi-steinmetz-naomi-jaffe-otzar
```
2. **Check directory:**
   ```
   finalproject-10-lin-abi-steinmetz-naomi-jaffe-otzar/
   ├── DEVLOGS/
   │   ├── DEVLOG-Abigail.md
   │   ├── DEVLOG-Naomi.md
   │   ├── DEVLOG-Otzar.md
   ├── README.md
   ├── data/
   │   ├── audio.wav
   │   ├── data.txt
   ├── images/
   │   ├── image1.jpg
   │   ├── image2.jpg
   ├── lsb/
   │   ├── decode.py
   │   ├── encode.py
   └── makefile
   ```
3. **Encode a message:**
You will be prompted to input the neccessary parameters: .wav audio file, .txt secret message, and which LSB encoding mode.

Python 3: ```make encode```

Python: ```make encode2```

4. **Decode a message:**
For decode, you will need to give the .wav file to decode. The program will prompt you for which decoding LSB mode you would like to use.

Python 3: ```make decode ARGS="(.wav file)"```

Python: ```make decode2 ARGS="(.wav file)"```

5. **Compare audio files:**
You will be prompted to input the necessary parameters: original .wav audio file and modified .wav audio file.

Python 3: ```make compare ARGS```

Python: ```make compare2 ARGS```

## Resources/ References:

https://svenruppert.com/2024/04/17/audio-steganography-in-more-detail/

### **Documentation:**
https://docs.python.org/3/library/wave.html<br>
https://docs.python.org/3/library/os.html<br>
https://docs.python.org/3/library/sys.html

### **Audio Stegnography:**
https://svenruppert.com/2024/04/17/audio-steganography-in-more-detail/

### **LSB:**
https://daniellerch.me/stego/intro/lsb-en/
https://github.com/sniperline047/Audio-Steganography-CLI/tree/main/algorithms

### **Phase Coding:**
https://dsp.stackexchange.com/questions/14804/audio-steganography-using-phase-encoding-technique
