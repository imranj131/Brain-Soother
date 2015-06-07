import pyaudio
import time
import numpy as np
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 0.1  # in seconds, may be float
f1 = 200.0        # sine frequency, Hz, may be float
f2 = 400		# sine2 frequency

pauseTime = 0.01



#Smooothing array to multiply the sineWave by
#smoother = np.asarray(range(softWindow,0,-1))/softWindow

#generate samples, note conversion to float32 array
sineWave1 = (np.sin(2*np.pi*np.arange(fs*duration)*f1/fs)).astype(np.float32)
sineWave2 = (np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)).astype(np.float32)
#sineWave[0:softWindow] = sineWave[0:softWindow]*smoother
#sineWave[-softWindow-1:-1] = sineWave[-softWindow-1:-1]*smoother




# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
a = 0
beats = 0

timeOrigin = time.time()
timeAll = time.time()

while a < 1000:
	
	time.sleep(pauseTime)
	stream.write(sineWave1*volume)
	time.sleep(pauseTime)
	stream.write(sineWave2*volume)
	
	timeAll = np.append(timeAll,time.time())		
	beats +=1
	a += 1

timeAll = timeAll - timeOrigin
frequency = np.round((beats/timeAll[-1]))

stream.stop_stream()
stream.close()


p.terminate()