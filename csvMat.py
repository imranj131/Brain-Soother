# -*- coding: utf-8 -*-
import numpy as np

directory = '/home/phc/Dropbox/Hackathons/Brain-Soother/'
fileName = 'OpenBCI-RAW-PHIL.txt'

dataTxt = open(directory+fileName)
dataString = dataTxt.read()

lines = dataString.split('\n')

data = []

for l in lines[5:]:
	data.append(l.split(', '))

for i in range(0,len(data)-1):
	for j in range(0,len(data[i])-1):
		data[i][j] = float(data[i][j])
		
		
			
