import numpy as np
import matplotlib.pyplot as plt

RECORD_TIME = 0.2
RATE = 44100
CHUNK = RATE/30

storage = np.load('OnToOff.npy')

plt.figure(1)
plt.plot((np.arange(storage.size/2)*(CHUNK/(RATE*RECORD_TIME))),storage)
plt.show()
