from __future__ import division
from matplotlib import pylab
from pylab import *
import numpy as np
from scipy import *
import scipy.io.wavfile

def index_of_max( tab ):
	index = 0
	maks = tab[0]
	
	for i in range(len(tab)):
		if(maks < tab[i]):
			maks = tab[i]
			index = i
	return index
		
	

np.set_printoptions(threshold=np.nan)
w, signal = scipy.io.wavfile.read('003_K.wav')
n = len(signal)

sound_time = n/w
t = linspace(0, sound_time, n, endpoint=False)
#t = arange(0, sound_time, 1/w)

#subplot(311)
#plot(t, signal, '*')
#xlabel("Probki")
#ylabel("Signal[t]")

signal1 = fft(signal)*2/n
signal1 = abs(signal1)
freqs = linspace(0, w, n, endpoint=False)

#subplot(312)
#plot(freqs, signal1, '-*')
#xlabel("w [Hz]")
#ylabel('fft(signal)')

#[rxx, lags] = xcorr(signal, signal, maxlags = len(signal))

#rxx_lags = xcorr(signal, signal, maxlags=2 )
#rxx = rxx_lags[0]
#lags = rxx_lags[1]


rxx = np.correlate(signal, signal,"full")
#lags = linspace(-len(signal) + 1, len(signal) - 1, len(signal)*2 - 1 )


first_pick_lock = len(signal) + 1

half_min = 15

seq = rxx
i = first_pick_lock - half_min
j = first_pick_lock + half_min
seq[i : j] = min(seq)

max_value = max(seq)
second_pick_lock = index_of_max(seq)

period = abs(second_pick_lock - first_pick_lock)

print(first_pick_lock)
print(rxx[first_pick_lock])
print(index_of_max(rxx))
print(max(rxx))
'''
print('MAX:')
print(max(rxx))

print('index max')
print(index_of_max(rxx))

print("srodek")
print(rxx[len(signal) + 1])

print("index srodek")
print(len(signal) + 1)

print("Last index")
print(len(rxx) - 1)
'''
#subplot(313)

#show()
