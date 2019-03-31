import pyaudio
import numpy as np
np.set_printoptions(suppress=True) # don't use scientific notation

RECORD_TIME = 0.2 # number of seconds to record as one snippet
RATE = 44100 # time resolution of the recording device (Hz)
CHUNK = int(RATE/20) # number of data points to read at a time 
TARGET1 = 900 # target frequency to be used as feedback
TARGET2 = 1200
#900 can be used to determine if a decent signal is seen, but 1200 allows us to capture signals which have a higher
#frequency sound which is more desireable
NOISE1 = 3000 # frequencies to watch which will only contain high power
NOISE2 = 5000   # when noise is present

def getPower(p,stream):
    goodSignalPower = np.array([]) # create a numpy array to hold the power oat the target frequency in each snippet
    betterSignalPower = np.array([]) # create a numpy array to hold the power oat the target frequency in each snippet
    noise1Arr = np.array([])
    noise2Arr = np.array([])
    for i in range(int((RATE/CHUNK)*RECORD_TIME)): # record as many chunks to make one snippet
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        fft = abs(np.fft.fft(data).real)
        fft = fft[:int(len(fft)/2)] # keep only first half
        freq = np.fft.fftfreq(CHUNK,1.0/RATE)
        freq = freq[:int(len(freq)/2)] # keep only first half
        assert freq[-1]>TARGET1, "ERROR: increase chunk size"
        goodSignal = fft[np.where(freq>TARGET1)[0][0]]
        betterSignal = fft[np.where(freq>TARGET2)[0][0]]
        noise1 = fft[np.where(freq>NOISE1)[0][0]]
        noise2 = fft[np.where(freq>NOISE2)[0][0]]
        if noise1 > 2000 or noise2 > 2000:
            goodSignal = 0
            betterSignal = 0
        goodSignalPower = np.append(goodSignalPower,goodSignal)
        betterSignalPower = np.append(betterSignalPower,betterSignal)
        noise1Arr = np.append(noise1Arr,noise1)
        noise2Arr = np.append(noise2Arr,noise2)
        print(noise1)
#        print(goodSignalPower,", ",betterSignalPower)
#    return np.array([(np.sum(goodSignalPower)/int((RATE/CHUNK)*RECORD_TIME)),(np.sum(betterSignalPower)/int((RATE/CHUNK)*RECORD_TIME))])
    return noise1Arr

if __name__ == "__main__":
    storage = np.array([[0,0]])

    p=pyaudio.PyAudio() # start the PyAudio class
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK) #uses default input device
    
    try:
        while True:
            storage = np.append(storage,[getPower(p,stream)])#,axis=0)
#            print(storage[int((storage.size/2)-1),0],", ",storage[int((storage.size/2)-1),1])
##            if storage[storage.size - 1][0] > 100000:
##                print(1)
##            else:
##                print(0)
    except KeyboardInterrupt:
        # close the stream gracefully
        stream.stop_stream()
        stream.close()
        p.terminate()

        np.save("Noise",storage)
        pass
