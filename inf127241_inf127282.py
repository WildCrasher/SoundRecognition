from __future__ import division
from matplotlib import pylab
from pylab import *
from scipy import *
from scipy import signal
import numpy as np
import scipy.io.wavfile
import subprocess
import sys

#functions

def index_of_max( tab ):
	index = 0
	maks = tab[0]
	
	for i in range(len(tab)):
		if(maks < tab[i]):
			maks = tab[i]
			index = i
	return index
		

#main

w, voice = scipy.io.wavfile.read(sys.argv[1])

if ( len(np.shape(voice)) > 1 ) :
	voice = [ s[0] for s in voice]
	voice = np.asarray(voice)

n = len(voice)
threshold = 380

rxx = signal.fftconvolve(voice,voice[::-1],mode = "full")
rxx = rxx[(len(rxx)//2)-1:]

extrema_max_indexes = signal.argrelextrema(rxx,np.greater)
extrema_max_indexes = extrema_max_indexes[0]

valid = []
for i in extrema_max_indexes:
	if w/i < threshold:
		valid.append(i)

pick_lock = valid[0]
temp_value_of_pick_lock = rxx[pick_lock]
fundamental_frequency = 0

pick_lock = index_of_max(rxx[valid])
fundamental_frequency = w/valid[pick_lock]

#male 85 - 180, female 165 - 255

if(fundamental_frequency <= 180):
	print("M")
else:
	print("K")
