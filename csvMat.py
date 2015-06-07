# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#directory = '/home/phc/Dropbox/Hackathons/Brain-Soother/'
fileName = 'OpenBCI-RAW-PHIL.txt'

dataTxt = open(fileName)
dataString = dataTxt.read()

lines = dataString.split('\n')

data = []

for l in lines[5:]:
	n = l.split(', ')[2]
	if n == "":
		n = 0
	else:
		n = float(n)
	data.append(n)

#for i in range(0,len(data)-1):
#	for j in range(0,len(data[i])-1):
#		data[i][j] = float(data[i][j])
		
#FFT = np.fft.fft(data[1000:])
#N = len(data)/2+1
#
##Time frequency domain
#plt.figure()
#plt.plot(abs(FFT[10:N]))
#freq  = 250 #sampling frequency
#
#X = np.linspace(0, N*1/freq, N, endpoint=True)
#
#
#plt.figure()
#plt.plot(X, 2*np.abs(FFT[:N])/N)
#plt.xlabel('Frequency ($Hz$)')
#			
