import numpy as np
#import matplotlib.pyplot as plt

#Will return the frequency with the highest amplitude

def meanFFT(data,minFQ=6,maxFQ=50):
	
	FFT = np.fft.fft(data)	
	
	N = len(FFT)/2+1
	freq = 250
	binSize = 100;
	X = np.linspace(0, freq/2, N, endpoint=True)
		
	#	FFT[X<=minFQ] = np.mean(FFT) THIS COULD BE FILTER
	#	FFT[X>=maxFQ] = np.mean(FFT) THIS COULD BE FILTER
	meanAmp = []
	meanFq = []
	
	Xmin = np.where(X >= minFQ)[0][0] #Find first value that is > minFQ
	Xmax = np.where(X < maxFQ)[0][-1]
	
	for bin in range(Xmin,Xmax,binSize):
		meanAmp.append(np.mean(np.abs((FFT[bin:bin+binSize-1]))))
		meanFq.append(np.mean(np.abs((X[bin:bin+binSize-1]))))
	
	frequency =  meanFq[np.where(meanAmp == np.max(meanAmp))[0][0]]
	frequency = np.round(frequency)
	
#	plt.figure()
#	plt.plot(X,abs(FFT[:N]))
#	plt.draw()
#	
	return frequency