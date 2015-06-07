# -*- coding: utf-8 -*-
import numpy as np

#directory = '/home/phc/Dropbox/Hackathons/Brain-Soother/'
def cleanData(fileName='OpenBCI-RAW-PHIL.txt', channel=2):

	dataTxt = open(fileName)
	dataString = dataTxt.read()
	
	lines = dataString.split('\n')
	
	data = []	
	
	n = 0
	
	for l in lines[5:-2]:
		n = l.split(', ')[channel-1]
		if n == "":
			n = 0
		else:
			n = float(n)
		data.append(n)

	return data