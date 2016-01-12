# WAVSteganography
Python program to hide and extract text in WAV files

The program works by splitting a WAV file in to chunks and writing data to the first frame of each chunk. 

To use:

Hide text file:
```bash
> python WAVSteganography.py hide message.txt source.wav hidden.wav
```

Extract to text file:
```bash
> python WAVSteganography.py extract hidden.wav message.txt
```
