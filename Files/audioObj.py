import ffmpy
import soundfile as sf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

class audioObj:
    
    def binary(self,i):
        bnr = bin(i).replace('0b','')
        x = bnr[::-1] #this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        return bnr 
    
    def mp3towav(self,src,dest):
        ff = ffmpy.FFmpeg(
            inputs={src: None},
            outputs={dest: None},global_options = ['-hide_banner','-loglevel panic'])
        ff.run()
        
    def wavtomp3(self,src,dest):
        if os.path.exists('DecodedSamples/decoded.mp3'):
            os.remove('DecodedSamples/decoded.mp3')
        ff = ffmpy.FFmpeg(
            inputs={src: None},
            outputs={dest: None},global_options = ['-hide_banner','-loglevel panic'])
        ff.run()
        
    def openaudio(self,filename):
        with open(filename,'rb') as f:

            while f.readable():
                if f.read(1):
                    print (f.read(1))
                else:
                    break
                    
    def mp3tobits(self,filename):
        if os.path.exists('EncodingSamples/Sound/mp3towav/con.wav'):
            os.remove('EncodingSamples/Sound/mp3towav/con.wav')
        self.mp3towav(filename,'EncodingSamples/Sound/mp3towav/con.wav')
        return self.wavtobits('EncodingSamples/Sound/mp3towav/con.wav')
                    
    def wavtobits(self,filename):
            data, samplerate = sf.read(filename,dtype='int16')
            
            if data.ndim == 1:
                nddata = np.transpose(data)
                nddata = nddata + 32768
                nddata = nddata/256
                nddata = nddata.astype('uint8')
                binary_d = []
                for i in nddata:

                    binary_d.append(self.binary(i))

                samplerate = int(samplerate/256)
                b_str = ''.join(binary_d)
                b_str = str(self.binary(samplerate))+b_str
                return b_str


            elif data.shape[1] == 2:
                data = data.flatten()
                nddata = np.transpose(data)
                nddata = nddata + 32768
                nddata = nddata/256
                nddata = nddata.astype('uint8')
                test2 = nddata
                binary_d = []
                for i in nddata:

                    binary_d.append(self.binary(i))

                samplerate = int(samplerate/256)
                b_str = ''.join(binary_d)
                b_str = str(self.binary(samplerate))+b_str
                test = b_str
                return b_str
            
    def bitstomp3(self,st):
        self.bitstowav(st,channel=2)
        self.wavtomp3('DecodedSamples/Decode.wav','DecodedSamples/decoded.mp3')
    
    def bitstowav(self,st,channel=1):
        
        if channel==1:
            h_bits = [st[i:i+8] for i in range(0, len(st), 8)]
            i = [int(j,2) for j in h_bits]
            samplerate = i[0]*256
            data = np.array(i[1:])*256
            data = data - 32768
            npdata = data.astype('int16')

            sf.write("DecodedSamples/Decode.wav",npdata, samplerate)
            return 1
        elif channel==2:
            h_bits = [st[i:i+8] for i in range(0, len(st), 8)]
            i = [int(j,2) for j in h_bits]
        
            samplerate = i[0]*256
            data = np.array(i[1:])*256
            data = data - 32768
            data = data.astype('int16')
            data = data.reshape(data.shape[0]//2,2)
            
            
            sf.write("DecodedSamples/Decode.wav",data, samplerate)
            return 1