import pyaudio
import time
import numpy as np



def soundGenerator(freq = 10, stimDur = 1, f1 = 200, f2 = 400, vol = 1):
	
	p = pyaudio.PyAudio()
	
	fs = 44100       # sampling rate, Hz, must be integer
	dur = 0.1  # in seconds, may be float
	
	freqEstim = np.asarray(range(1,100))
	freqEstim = freqEstim/1000.0 + 0.01
	
	if freq >= 25:
		freq = 24
		
	pauseTime = freqEstim[99-4*freq]
	
	#generate samples, note conversion to float32 array
	sineWave1 = (np.sin(2*np.pi*np.arange(fs*dur)*f1/fs)).astype(np.float32)
	sineWave2 = (np.sin(2*np.pi*np.arange(fs*dur)*f2/fs)).astype(np.float32)	
		
	# for paFloat32 sample values must be in range [-1.0, 1.0]
	stream = p.open(format=pyaudio.paFloat32,
	                channels=1,
	                rate=fs,
	                output=True)
	
	# play. May repeat with different volume values (if done interactively) 
	beats = 0
	
	t1 = time.time()
	t2 = t1
	
	while t2-t1 <= stimDur:
		
		time.sleep(pauseTime)
		stream.write(sineWave1*vol)
		time.sleep(pauseTime)
		stream.write(sineWave2*vol)
		
		t2 = time.time()
			
		beats +=1
	
	frequency = np.round((beats/(t2-t1)))
	
	stream.stop_stream()
	stream.close()
	p.terminate()