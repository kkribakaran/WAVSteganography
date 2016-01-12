#Karthik Kribakaran
#Jan 2016
from __future__ import division
import wave, struct, sys, getopt


def hide(textfile,wavfile,hiddenfile):
    text = open(textfile, 'r')
    contents = text.read()
    contentslength = len(contents)  #number of chars in text file
    if (contentslength == 0):
        print("Empty text file")
        sys.exit()
    sourcewav = wave.open(wavfile,'r')
    outputwav = wave.open(hiddenfile, 'w')
    outputwav.setparams(sourcewav.getparams())
    framecount = sourcewav.getnframes() #number of frames in wav file
    if (contentslength > 99999999):
        print("Text file too large")
    if (contentslength > framecount/2):
        print("Sound file not large enough")
        sys.exit()
    chunklength = framecount // (contentslength+1) #number of frames per chunk. first frame of chunk contains text data, other chunklength-1 frames contain audio data
    temp = contentslength #value of first frame in first chunk is length of text file
    sourcewav.readframes(1)
    frame = ''
    for i in range(0,4):
        if (temp > 0):
            frame+= chr(temp%100)
        else:
            frame+= chr(0)
        temp = temp // 100
    outputwav.writeframes(frame) #writes length of text file
    outputwav.writeframes(sourcewav.readframes(chunklength-1)) #fills rest of chunk with audio data
    for i in range(0, contentslength):
        y = sourcewav.readframes(1)
        frame = ''
        frame += contents[i] #reads char from text file and writes to first index of the first frame of the chunk 
        for j in range(1,4):
            frame += y[j] #fills other indeces with audio data
        outputwav.writeframes(frame) #writes first frame
        outputwav.writeframes(sourcewav.readframes(chunklength-1)) #fills rest of chunk with audio data
    outputwav.writeframes(sourcewav.readframes(framecount % contentslength)) #writes remaining audio data 
    sourcewav.close()
    outputwav.close()
    text.close()

def extract(hiddenfile,message):
    text = open(message, 'w')
    sourcewav = wave.open(hiddenfile,'r')
    framecount = sourcewav.getnframes() #number frames in wav file
    frame = sourcewav.readframes(1)
    contentslength = ord(frame[0]) + 100*(ord(frame[1])) + 10000*(ord(frame[2])) + 1000000*(ord(frame[3])) #grabs text length from first frame of audio
    chunklength = framecount // (contentslength+1) 
    sourcewav.readframes(chunklength-1)
    for i in range(0, contentslength):
        text.write(sourcewav.readframes(1)[0]) #reads first index of first frame of current chunk, writes to text file
        sourcewav.readframes(chunklength-1) #reads past regular audio data
    sourcewav.close()
    text.close()

def main(argv):
    textfile = ''
    wavfile = ''
    hiddenfile = ''
    message = ''
    if (len(sys.argv) == 5 and sys.argv[1] == 'hide'):
        textfile = sys.argv[2]
        wavfile = sys.argv[3]
        hiddenfile = sys.argv[4]
        hide(textfile,wavfile,hiddenfile)
    elif (len(sys.argv) == 4 and sys.argv[1] == 'extract'):
        hiddenfile = sys.argv[2]
        message = sys.argv[3]
        extract(hiddenfile,message)
    else:
        print('Usage: WAVSteganography.py hide <textfile> <wavefile> <resultwavefile>\nUsage: WAVSteganography.py extract <wavefile> <resulttextfile>')
    
if __name__ == '__main__':
    main(sys.argv[1:])
