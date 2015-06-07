# -*- coding: utf-8 -*-
import numpy as np

#directory = '/home/phc/Dropbox/Hackathons/Brain-Soother/'
def cleanData(fileName='OpenBCI-RAW-PHIL.txt'):

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

	return data