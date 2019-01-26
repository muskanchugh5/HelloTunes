pianoKeys={
"a0":27.5, 
"a-0":29.1, 
"b0":30.9, 
"c1":32.7, 
"c-1":34.6, 
"d1":36.7, 
"d-1":38.9, 
"e1":41.2, 
"f1":43.7, 
"f-1":46.2, 
"g1":49.0, 
"g-1":51.9, 
"a1":55.0, 
"a-1":58.3, 
"b1":61.7, 
"c2":65.4, 
"c-2":69.3, 
"d2":73.4, 
"d-2":77.8, 
"e2":82.4, 
"f2":87.3, 
"f-2":92.5, 
"g2":98.0, 
"g-2":103.8, 
"a2":110.0, 
"a-2":116.5, 
"b2":123.5, 
"c3":130.8, 
"c-3":138.6, 
"d3":146.8, 
"d-3":155.6, 
"e3":164.8, 
"f3":174.6, 
"f-3":185.0, 
"g3":196.0, 
"g-3":207.7, 
"a3":220.0, 
"a-3":233.1, 
"b3":246.9, 
"c4":261.6, 
"c-4":277.2, 
"d4":293.7, 
"d-4":311.1, 
"e4":329.6, 
"f4":349.2, 
"f-4":370.0, 
"g4":392.0, 
"g-4":415.3, 
"a4":440.0, 
"a-4":466.2, 
"b4":493.9, 
"c5":523.3, 
"c-5":554.4, 
"d5":587.3, 
"d-5":622.3, 
"e5":659.3, 
"f5":698.5, 
"f-5":740.0, 
"g5":784.0, 
"g-5":830.6, 
"a5":880.0, 
"a-5":932.3, 
"b5":987.8, 
"c6":1046.5,
"c-6":1108.7,
"d6":1174.7,
"d-6":1244.5,
"e6":1318.5,
"f6":1396.9,
"f-6":1480.0,
"g6":1568.0,
"g-6":1661.2,
"a6":1760.0,
"a-6":1864.7,
"b6":1975.5,
"c7":2093.0,
"c-7":2217.5,
"d7":2349.3,
"d-7":2489.0,
"e7"0:2637.0, 
"f7":2793.8, 
"f-7":2960.0, 
"g7":3136.0, 
"g-7":3322.4, 
"a7":3520.0, 
"a-7":3729.3, 
"b7":3951.1, 
"c8":4186.0, 
}
 


import tensorflow as tf
import numpy as np
import pandas as pd

from pyAudioAnalysis import audioBasicIO 
from pyAudioAnalysis import audioFeatureExtraction 
import matplotlib.pyplot as plt

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file("raat.mp3")
song.export("converted_audio5.wav", format="wav", bitrate="128k")
[Fs,x]=audioBasicIO.readAudioFile('converted_audio5.wav') 


freqList=[]
min=13000
keys=[]


from scipy import signal
f, t, Zxx = signal.stft(x, Fs,nperseg=Fs)

max=0
prevMax=0
index=0
for j in range(t.shape[0]):
    for i in range(f.shape[0]):
        if Zxx[i][j]>max:
            prevMax=max
            max=Zxx[i][j]
            prevInd=index
            index=i
    if max-prevMax<10:
        freqList.append(list(f[index],f[prevInd]))
    else:
        freqList.append(f[index])




for f in freqList:
    for key in pianoKeys:
        diff=abs(pianoKeys[key]-f)
        if(diff<min):
            min=diff
            keyNo=key
    keys.append(keyNo)
