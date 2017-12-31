from __future__ import division
from matplotlib import pylab
from pylab import *
import numpy as np
from scipy import *
import scipy.io.wavfile

#functions

def index_of_max( tab ):
	index = 0
	maks = tab[0]
	
	for i in range(len(tab)):
		if(maks < tab[i]):
			maks = tab[i]
			index = i
	return index
		
	
def find_first_min( rxx, first_pick_lock ):
	i = first_pick_lock + 1
	j = first_pick_lock - 1
	while (rxx[i - 1] > rxx[i]) and (rxx[j + 1] > rxx[j]):
		i += 1
		j -= 1
	return i - 1

#main

np.set_printoptions(threshold=np.nan)
w, signal = scipy.io.wavfile.read('006_K.wav')
n = len(signal)
T = 1/w
sound_time = n/w

t = linspace(0, sound_time, n, endpoint=False)

signal1 = fft(signal)*2/n
signal1 = abs(signal1)

rxx = np.correlate(signal/1000, signal/10000, "full")

first_pick_lock = len(signal) - 1

right_min_index = find_first_min(rxx, first_pick_lock) 
left_min_index = first_pick_lock - ( right_min_index - first_pick_lock )

seq = rxx
i = right_min_index
j = left_min_index

seq[j : i] = min(seq)

#max_value = max(seq)
second_pick_lock = index_of_max(seq)

period_in_samples = abs(second_pick_lock - first_pick_lock)
print(period_in_samples)
print(T)

period = period_in_samples * T
fundamental_frequency = 1/period
print(fundamental_frequency)

#male 85 - 180, female 165 - 255

if(fundamental_frequency <= 165):
	print("M")
elif(fundamental_frequency >= 180):
	print("K")
else:
	print("Not sure")
