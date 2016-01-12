# WAVSteganography
Python program to hide and extract text in WAV files. The resulting WAV file carrying text will sound nearly identical to the source. The program works by splitting a WAV file in to chunks and writing data to the first frame of each chunk. 


Hide text file: 
```bash
> python WAVSteganography.py hide message.txt example.wav hidden.wav
```

Extract to text file:
```bash
> python WAVSteganography.py extract hidden.wav message.txt
```
